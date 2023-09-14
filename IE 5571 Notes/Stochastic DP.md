September 13, 2023
#knowledge 

---

Model: $x_{n+1}=f()$
{A}

### Two differences between stochastic and deterministic DP
1. In deterministic DP system states are completely determined by control choices
- In stochastic DP problem, we do not know what states we will visit ahead of time
- We do need to specify "policies" that tell us what to do in each state. 
- Policy $\mu^{*}_k(x)$: optimal action when in state $x$ at stage $k$
2. Evaluating objective function requires evaluating an expected value

### Solution to the stochastic DP problem is
{B}
Can solve using a DPE
$V_N(x)=g_N(x)$ for all $x$ 
for $n\in\{0,1,...N-1\}$
{C}, solve for all $x$
store minimizing argument, $u^*(x)$ as $\mu_n^*(x)$ 
Can show that $V_0{x}=J^*(x)$ all $x$

# Example
- Agents starts with wealth $X_0$
- At each stage $n\in\{0,1,..,N-1\}$ agent consumes proportion $u_n$ of wealth
- Remainder gets into back and earns interest at rate $r_n$ {this is now a random variable}
- $\{r_n\}_{n\geq1}$ are a sequence of i.i.d. RV's
- $R_n=1+r_n$
- $X_{n+1}=R_{n}X_{n}(1-u_n)$
- Consuming wealth $x$ at stage  $n\in\{0,1,..,N-1\}$ gives utility $g(x)$ and at stage $N$ gives utility $g_N(x)$ 
- {D}
- goal choose $u_{0},u_1,...u_n$ to maximize $J$
$n=N-1$, wealth $x$
{E}
max possible utility for wealth $x$ at stage $N-1$:
{}
max $u_{n-1}$ will give optimal policy at stage $n-1$
For $n=0,1,...N-1$
{}
$V_0(x)$=max possible utility starting from wealth $x$

((Infinite horizon problem can sometimes be easier because no time factor))
((finite horizon problems can be a bit harder - retirement))


