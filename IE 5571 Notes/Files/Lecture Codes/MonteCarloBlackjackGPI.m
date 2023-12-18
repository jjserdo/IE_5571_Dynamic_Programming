function [Pol,ValFun]=MonteCarloBlackjackGPI(MCNum)
%Use monte-carlo simulation and GPI to approximate optimal policy.
Count=zeros(480,1);
Pol=zeros(12,10,2);
Pol(1,:,:)=ones(10,2); %Will always hit when sum of cards is <=11
Q=zeros(12,10,2,2); %Q(s,a)
%Returns=zeros(200,1);
for j=1:MCNum
    [Tr_state,Tr_action,Tr_reward]=BlackjackSim2(Pol);
    L=length(Tr_state(1,:));
    G=0;
    for l=L:-1:1
        G=G+Tr_reward(l);
        S=Tr_state(1,l);
        Ace=Tr_state(2,l);
        Deal=Tr_state(3,l);
        a=Tr_action(l);
        I=sub2ind([12 10 2 2],S-10,Deal,Ace+1,a+1);
        Count(I)=Count(I)+1;
        Q(S-10,Deal,Ace+1,a+1)=Q(S-10,Deal,Ace+1,a+1)+(G-Q(S-10,Deal,Ace+1,a+1))/Count(I);
        if S>11 && S<21
        [~,Pol(S-10,Deal,Ace+1)]=max([Q(S-10,Deal,Ace+1,1) Q(S-10,Deal,Ace+1,2)]);
        end
    end
end
[ValFun,Pol]=max(Q,[],4);


%plot average reward
NoUsableAce=zeros(10,10);
UsableAce=zeros(10,10);
Pol_noAce=zeros(10,10);
for i=2:11
    for j=1:10
        I1=sub2ind([12 10],i,j);
        NoUsableAce(i-1,j)=ValFun(I1);
        Pol_noAce(i-1,j)=Pol(I1);
        UsableAce(i,j)=ValFun(I1+120);
    end
end
%plot of value function
surf(1:10,12:21,NoUsableAce)
figure
%plot of optimal policy
imagesc(1:10,12:21,Pol_noAce)