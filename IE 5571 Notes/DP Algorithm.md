September 6, 2023
#lecture #knowledge 

---

DP Algorithm is based on the [[DP Principle]]

Let $u^*=(u^*_0,u^*_1,...,u^*_{N-1})$ be an optimal control sequence
and $x^*=(x^*_0,x^*_1,...,x^*_N)$ be the optimal state sequence

If we start at $x^*_k$ at stage $k$ and we want to minimize the remaining cost
$g_k(x^*_k,u_k)+\sum^{N-1}_{m=k+1}g_m(x_m,u_m)+g_N(x_N) \; \; (*)$
--> minimize the cost going forward

![[Pasted image 20230907214550.png]]

then the solution is $(u^*_k,u^*_{k+1},...,u^*_{N-1})$

#### Proof
If  the solution to $(*)$ was
$(\tilde{u}^*_k,\tilde{u}^*_{k+1},...,\tilde{u}^*_{N-1})$
then
I could make a new control
$\hat{u}=(u^*,...,u_{k-1}^*, tildes)$
and $J(x_0;<\hat{u})<J(x_0;u^*)$ 
contradicting the optimality of $u^*$
Problem $(*)$ is called the [[Tail Subproblem]] of length N-K