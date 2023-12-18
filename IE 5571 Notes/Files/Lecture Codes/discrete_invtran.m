function X=discrete_invtran(pmf)
%Generates samples from random variable X with pmf given by pmf.

pmf=pmf/sum(pmf); %make sure that pmf sums to 1.
n=max(size(pmf)); %number of possible values RV X can take.
F=pmf(1); %probability RV takes its smallest value.
U=rand; 
i=1; %initialize counter.
exit=0; %condition for exiting loop.
while (exit==0)
    if U<F
        X=i;
        break;
    else
        F=F+pmf(i+1);
        i=i+1;
    end
    if (i==n)
        X=i;
        break
    end
end

        
