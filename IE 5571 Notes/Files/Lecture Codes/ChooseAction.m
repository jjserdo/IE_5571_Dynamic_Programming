function Action=ChooseAction(U)
%choose action based on U
if U==1
    Action=[1 0];
elseif U==2
    Action=[0 1];
elseif U==3
    Action=[-1 0];
else
    Action=[0 -1];
end