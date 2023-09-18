
#book #knowledge 
Reinforcement Learning
Sutton & Barto
ppdf 47
Chapter 2

---

- *evaluates* rather than *instructs*

## A k-armed Bandit Problem
- each action ($A_t$) has an expected or mean reward *value* ($R_t$)
- *greedy* takes the highest estimated value: *exploiting* - maximize reward on one step
- *exploring* - takes non-greedy action to maybe maximize the expected reward in the long run
### Action-value Methods
- *action-value methods* - true value of an action is the mean reward when that action is selected; averaging the rewards actually received
![[Pasted image 20230912105252.png]]


---

[[Lecture 3  Notes]] September 13, 2023 
#lecture 

- We have $k$ slot machines each with a different probability distribution for earnings
- We get to play machines repeatedly
- Each turn we choose a machine to play
- Goal: maximize expected total reward over a large number of plays

- We choose arms (machines) at times $t=1,2,...$
- Our action at time $t$ is given by $A_t\in\{1,..k\}$ assuming $k$ arms
- Reward on time step $t$ is $R_t$
- for each $a\in\{1,.,.k\}$ interested in $q_{*}(a)=E(R_t|A_t=a)$
- We don't know $q_*(a)$, if we knew $q_*(a)$ we would always choose $A_t=argmax_{a\in\{1,..k\}}(q_*(a))$ 
- At time $t$ we estimate $q_*(a)$ with $Q_t(a)$. Hopefully $Q_t(a)\approx{q_*(a)}$ 
- Given $Q_t(a);a\in\{1,..k\}$ we can always make a "greedy" choice
$A_t=argmax_{a\in\{1,..k\}}(Q_t(a))$ but ((there could be another machine out there that is better))
- Since $Q_t$ is just an estimate it makes sense to sometimes "explore" instead of just the greedy choice
	- e.g. suppose we know $q_*(1)\in(4.9,5.1)$ with high probability and $q*(2)\in(2.5,6.5)$ with high probability
	- $Q_b(1)=5$, and $Q_t(2)=4$
	- Based on greedy choice we will always choose arm 1. But given uncertainty in $Q_t(2)$ it is possible $q_*(2)>q_x(1)$
	- ((greedy is also called exploit))
We will form $Q_t(a)$ by averaging rewards from arm $a$
For each $a\in\{1,.,.k\}$
$$Q_t(a)=\frac{\mathrm{total\;reward\;when\;using\;'a'\;prior\;to}\;t}{}$$
[[Law of Large Numbers]] 
{}

- When taking greedy action: {}

---
### $\epsilon$ - greedy approach
Fix $\epsilon\in(0,1)$, at each step with prob. $1-\epsilon$ we choose 
$$A_t\in{}argmax_aQ_t(a)$$
and with probability (w.p.) $\epsilon$ we choose $A_t$ at random from $\{1,.,.k\}$
((as t approaches infinity, we want to maybe reduce epsilon to 0))
((with epsilon fixed, it will explore everything))

---

## Updating Sample Averages
{}


---

## $\epsilon$ - greedy algorithm with averaging
{}


---

[[Lecture 4 Notes]] 
Last class we said estimate 