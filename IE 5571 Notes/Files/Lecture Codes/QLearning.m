function [Q,Pol,TotalReward]=QLearning(alpha,N_episodes)
%runs Qlearning algorithm with TD updates based at level alpha.
%run N_episodes total episodes
eps_0=0.3; %initial value for epsilon.
Q=zeros(48,4); %initialize Q as all zeros.
Pol=zeros(48,4); %initialize policy as all zeros.
GridH=4;
GridW=12;
%identify terminal state
TotalReward=zeros(N_episodes,1);
S_term=sub2ind([GridH,GridW],4,12);
S_0=sub2ind([GridH,GridW],4,1);
AvailActions=[1 2 3 4]; %can't go left on step 1.
pmf=[1 1 1 1];
for n=1:N_episodes
    eps=eps_0/n;
    S=S_0;
    
    j=0;
    while 1
        j=j+1;
        u=rand;
        if u<eps
            I=discrete_invtran(pmf);
            ActionInd=AvailActions(I);
        else
            [~,ActionInd]=max(Q(S,:));
        end
        Action=ChooseAction(ActionInd);
        [S_new,R]=GridWorldStep(S,Action);
        Q(S,ActionInd)=Q(S,ActionInd)+alpha*(R+max(Q(S_new,:))-Q(S,ActionInd));
        S=S_new;
        if S==S_term
            break;
        end
        TotalReward(n)=TotalReward(n)+R;
    end
    
end

for j=1:48
    m=max(Q(j,:));
    I=find(Q(j,:)==m);
    Pol(j,I)=1/length(I);
end
% M=zeros(GridH,GridW);
% for k=1:GridH*GridW
%     [r,c]=ind2sub([GridH,GridW],k);
%     M(r,c)=P
%
