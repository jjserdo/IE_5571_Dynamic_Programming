function [Q,Pol,EpLength]=Sarsa(alpha,N_episodes)
%runs Sarsa algorithm with TD updates based at level alpha.
%run N_episodes total episodes
eps_0=.3; %initial value for epsilon.
Q=zeros(70,4); %initialize Q as all zeros.
Pol=zeros(70,4); %initialize policy as all zeros.
GridH=7;
GridW=10;
%identify terminal state
S_term=sub2ind([GridH,GridW],4,8);
S_0=sub2ind([GridH,GridW],4,1);
EpLength=zeros(N_episodes,1);
for n=1:N_episodes
    eps=eps_0/n;
    %eps=eps_0/3;
    S=S_0;
    u=rand;
    AvailActions=[1 2 4]; %can't go left on step 1.
    pmf=[1 1 1];
    if u<eps
        I=discrete_invtran(pmf);
        ActionInd=AvailActions(I); 
    else
        [~,ActionInd]=max(Q(S,:));
    end
    Action=ChooseAction(ActionInd);
    j=0;
    while 1
        j=j+1;
%         if n==N_episodes
%             [Pos(j,1),Pos(j,2)]=ind2sub([GridH,GridW],S);
%         end
        S_new=GridWolrdStep(S,Action);
        AvailActions=[1 2 3 4];
        [r,c]=ind2sub([GridH,GridW],S_new);
        if r==1
            AvailActions(2)=[];
        elseif r==GridH
            AvailActions(4)=[];
        end
        if c==1
            AvailActions(3)=[];
        elseif c==GridW
            AvailActions(1)=[];
        end
        if S_new==S_term
            R=1;
        else
            R=-1;
        end
        pmf=ones(length(AvailActions),1);
        u=rand;
        if u<eps
            I=discrete_invtran(pmf);
            ActionIndNew=AvailActions(I);
        else
            [~,ActionIndNew]=max(Q(S_new,:));
        end
        ActionNew=ChooseAction(ActionIndNew);
        Q(S,ActionInd)=Q(S,ActionInd)+alpha*(R+Q(S_new,ActionIndNew)-Q(S,ActionInd));
        S=S_new;
        Action=ActionNew;
        ActionInd=ActionIndNew;
        if S==S_term
            break;
        end
    end
    EpLength(n)=j;
end

for j=1:70
    m=max(Q(j,:));
    I=find(Q(j,:)==m);
    Pol(j,I)=1/length(I);
end
% M=zeros(GridH,GridW);
% for k=1:GridH*GridW
%     [r,c]=ind2sub([GridH,GridW],k);
%     M(r,c)=P
%
