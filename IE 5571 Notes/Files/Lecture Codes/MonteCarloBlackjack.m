function AvgReward=MonteCarloBlackjack(MCNum)
%Use monte-carlo simulation to estimate value function at each possible
%state. 200 possible states.
AvgReward=zeros(200,1);
Count=zeros(200,1);
%Returns=zeros(200,1);
for j=1:MCNum
    [Tr_state,~,Tr_reward]=BlackjackSim;
    L=length(Tr_state(1,:));
    G=0;
    for l=L:-1:1
        G=G+Tr_reward(l);
        S=Tr_state(1,l);
        A=Tr_state(2,l);
        Deal=Tr_state(3,l);
        I=sub2ind([10 10 2],S-11,Deal,A+1);
        AvgReward(I)=AvgReward(I)+G;
        Count(I)=Count(I)+1;
    end
end
AvgReward=AvgReward./Count;
% M=min(Count);
% Ind=find(Count==M, 1, 'last' );
%plot average reward
NoUsableAce=zeros(10,10);
UsableAce=zeros(10,10);
for i=1:10
    for j=1:10
        I1=sub2ind([10 10],i,j);
        NoUsableAce(i,j)=AvgReward(I1);
        UsableAce(i,j)=AvgReward(I1+100);
    end
end
surf(1:10,12:21,NoUsableAce)