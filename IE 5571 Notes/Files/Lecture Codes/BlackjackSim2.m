function [Tr_state,Tr_action,Tr_reward]=BlackjackSim2(Pol)
%Generates a trajectory of a game of blackjack based on policy Pol.
%Pol is a 12 x 10 x 2 tensor.
%The first dimension is the sum of players cards, second dimension is
%dealers show card, and third dimension is 1 for usable ace 0 for no-usable
%ace.
%Q(i,j,k)=1 means stay in state (i,j,k), Q(i,j,k)=2 means hit in state
%(i,j,k).
Tr_state=zeros(3,22);%row 1 = sum, row 2 = 1 if usable ace 0 otherwise, row 3 = dealers show card
Tr_action=-3*ones(1,22);%hit = 1, stay = 0;
Tr_reward=-3*ones(1,22);
pmf=[ones(1,9) 4];
DHand=zeros(1,21);
PHand=zeros(1,21);
DHand(1:2)=[discrete_invtran(pmf) discrete_invtran(pmf)];
PHand(1:2)=[discrete_invtran(pmf) discrete_invtran(pmf)];
Pcards=2;
Dcards=2;
DShow=DHand(1);
t=1;
PInd=find(PHand==1, 1 );
useA=0;
D_useA=0;
if sum(PHand)-1<=10 && ~isempty(PInd)
    PHand(PInd)=11;
    useA=1;
end
DInd=find(DHand==1, 1 );
if sum(DHand)-1<=10 && ~isempty(DInd)
    DHand(DInd)=11;
    D_useA=1;
end
Tr_state(1,t)=sum(PHand);
Tr_state(2,t)=useA;
Tr_state(3,t)=DShow;
if sum(PHand)==21
    if sum(DHand)<21
        Tr_reward(t+1)=1;
    else
        Tr_reward(t+1)=0;
    end
    Tr_action(t)=0;
elseif rand<0.5
    Tr_action(t)=1;
else
    Tr_action(t)=0;
end


while Tr_action(t)==1 && Tr_reward(t+1)==-3
    t=t+1;
    PHand(Pcards+1)=discrete_invtran(pmf);
    Pcards=Pcards+1;
    if useA==1
        PHand(PInd)=1;
    end
    PInd=find(PHand==1, 1 );
    if sum(PHand)-1<=10 && ~isempty(PInd)
        PHand(PInd)=11;
        useA=1;
    else
        useA=0;
    end
    if sum(PHand)<22
        Tr_state(1,t)=max(sum(PHand),11);
        Tr_state(2,t)=useA;
        Tr_state(3,t)=DShow;
        if Pol(Tr_state(1,t)-10,Tr_state(3,t),Tr_state(2,t)+1)==2
            Tr_action(t)=1;
        else
            Tr_action(t)=0;
        end
    end
end
if sum(PHand)>21
    Tr_reward(t+1)=-1;
end

%dealer now plays


while sum(DHand)<17 && Tr_reward(t+1)==-3
    DHand(Dcards+1)=discrete_invtran(pmf);
    Dcards=Dcards+1;
    if D_useA==1
        DHand(DInd)=1;
    end
    DInd=find(DHand==1, 1 );
    if sum(DHand)-1<=10 && ~isempty(DInd)
        DHand(DInd)=11;
        D_useA=1;
    else
        D_useA=0;
    end
end

%Decide on game winner
if Tr_reward(t+1)==-3
    if sum(DHand)>sum(PHand) && sum(DHand)<22
        Tr_reward(t+1)=-1;
    elseif sum(DHand)==sum(PHand) 
        Tr_reward(t+1)=0;
    else
        Tr_reward(t+1)=1;
    end
end

I=find(Tr_state(1,:)>=12);
Tr_state=Tr_state(:,I);
Tr_action=Tr_action(I);
Tr_reward=[zeros(1,length(I)-1) Tr_reward(t+1)];