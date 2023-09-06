September 6, 2023
#lecture #knowledge 

---

Start with a discrete controlled dynamical system
## $x_{k+1}=f(x_k,u_k)$ where $k\in\{0,1,2,...,N-1\}$

, k is set of 0 to N-1
k - stage or time index
x_k - state of our system at time k
N - time horizon
u_k - control (or decision variable)
u_k is set of U(x_k)
-- things we are allowed to do at the current state
	-- can't drive on a red light or turn if in a bridge
f - mechanism that updates state variable
-- Introduce cost functions g_0, g_1, ... g_N to evaulate choice of controls u_0, u_1, .. u_N
-- Assume that costs are additive for condition x_0 and controls u_0, u1, .. u_{N-1} the cost of the control sequence is
## $J(x_0;u_0,u_1,...,u_{N-1})=g_N(x_N)+\sum^{N-1}_{k=0}g_k(x_k,u_k)$

-- only cost is at the end for hitting a friend with a water baloon
-- when in a space ship we might have a running cost
-- investment for retirement and stuff
-- self driving cars but not tesla

>can also be multiplicative cost

### $g_N(x_N)*\prod^{N-1}_{k=0}g_k(x_k,u_k)$

<insert picture 1 here>

Goal of optimal control is to solve
### $J^*(x_0)=min\{J(x;u_0,...,u_{N-1});u_K\in U(x_k),x_{k+1}=f(x_k,u_k)\}$

#### Example 1
<insert picture 2 here>

Goal: Find shortest length path from O to T
-- x_k or state: current node
-- k or stage: number of edges travelled
-- f or update mechanism: based on our graph
-- g_k or cost function: distance traveled on edge k
-- u_k or choices: choice of edge to travel
	-- can have a dynamic graph and maybe going backwards might be a good move

#### Example 2
To produce a product, 4 operations must be performed A,B,C,D
--> A must be performed before B
--> C must be performed before D
CDAB acceptable but CBAD is not
We given cost of transition from machine m to n: $C_{m.n}$
We have cost of starting at machine a or C: $S_A$ or $S_C$
The cost of ACDB would be: $S_A+C_{AC}+C_{CD}+C_{DB}$
Goal: Perform tasks to minimize cost
---! looks like [[Travelling salesman problem]]
---!---! looks like this but without the restrictions

--! The first two examples have a discreet state space
--! This next one is continuos
#### Example 3
A product passes through a sequence of N ovens
$x_0-initial\;temperature$
$x_k-temperature\;after\;leaving\;oven\;k=1,..,N$
$u_{k-1}-heat\;applied\;in\;oven\;k$
$x_{k+1}=(1-a)x_k+au_k\;,\;a\in(0,1)$
Goal: Temperature of product as close to T as possible while using little energy
#### $J(x_0;u_0,..,u_{N-1})=\sum^{N-1}_{k=0}u_k+|T-x_N|$
--> \alpha for abs or u_k <= T/N or use squared as well for both
#### $J(x_0;u_0,..,u_{N-1})=\sum^{N-1}_{k=0}u_k^2+\alpha(T-x_N)^2$
--> This has an exact solution
--> Called a [[Linear-quadratic control problem]] 

if product has to be kept below M temp
then ($1-a)x+au\leq\;M$

