September 11, 2023
#lecture 

---

#### Recall model from last class
$x_{k+1}=f(x_k,u,k)$, $k\in\{0,1,2,...,N\}$
$k$ - stage or time
$x_k$ - state of system at stage k
$f$ -  rule or function governing dynamics
$u_k$ - controls, $u\in{}U(x_k)$ - set of feasible controls
cost functions:  $g_{0},g_1,...g_N$ - running cost and terminal cost

###### For initial condition $x_0$ and control sequence
$u_0,..u_N$ cost is given by
$J(x_0;u_1,..u_N)=g_N(x_n)+\sum^{n-1}_{k=0}g_k(x_k,u_k)$

###### [Optimal Control Problem]
solve 
$J^*(x_0)=min\{J(x;u_0,...,u_{N-1});u_K\in U(x_k),x_{k+1}=f(x_k,u_k)\}$

###### Introduced [Tail Problem] for $k=0,1,..n$

Example 1: [[Wealth Problem]]
Example 2: [[Travelling Salesperson Problem]]

Small talk about stochastic dynamic programming
- don't know our state and can't predict
1. we try to minimize our expected utility/values
2. we need policies instead of controls
- smth that maps states to controls
- you need a function or policy
- don't know our state until you run the problem


