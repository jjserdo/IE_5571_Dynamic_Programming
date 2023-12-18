September 6, 2023
#lecture #knowledge 

---

### Overview of Dynamic Programming Algorithm
1. Solve tail subproblem involving last stage only
2. Solve *all* tail subproblems of length 1
	-- $min_{U_{N-1}}(g_{N-1}(x_{N-1},u_{N-1}+g(x_N))$
3. Solve all tail subproblem of length 2
...)
N-K) Solve all tail subproblem of length k

{September 13, 2023}
1. Solve tail problem with $k=N$
2. Solve tail problem with $k=N-1$ for all $x_{N-1}$
3. Solve tail problem with $k=N-2$, $\forall/x_{N-2}$
...
N-M. Solve all tail problem with $k=N-m$
...
N. Solve tail problem with $k=N$(???)