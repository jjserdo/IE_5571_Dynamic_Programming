
#example

---
September 13, 2023
##### Example 2
A salesperson is based in NYC and needs to visit Miami, Dallas, Chicago and then return to NYC. This is the following distance matrix.

|         | NYC  | Miami | Dallas | Chicago |
|---------|------|-------|--------|---------|
| NYC     |      | 1334  | 1559   | 809     |
| Miami   | 1334 |       | 1343   | 1397    |
| Dallas  | 1559 | 1343  |        | 921     |
| Chicago | 809  | 1397  | 921    |         |

What order to visit cities to minimize distance distance traveled?
We will use DP to solve the problem
stage j:  jth stop of trip
$j=0$, SP is in NYC, $j=4$, SP is in NYC
$x_j=(C_j,L)$, $C_j$ - current city; $L$- list of cities visited including $C_j$
$f_j(C_j,L)$ - minimal distance that must be traveled to complete the tour if SP is at jth stop in $C_j$and $L$ is all cities visited,
$d(I,J)$ - distance from city $I$ to city $J$ 
Can write DPE as 
$$f_j(C_j,L)=min_{J\notin{}L}\{d(C_j,L)+f_{j+1}(J,L \cup (J))\}$$
$L$ - doesn't care about order

$f_3(C_3,\{M,D,C\})=d(C_3,NYC)$
Using DPE
$f_2(C_2,L)=min_{J\&L}(d(C_2,J)+d(J,NYC))$

to use DPE we need to know $f_2$ at all possible states $(C_j,L)$
$f_2(M,\{M,D\})=d(M,C)+d(C,N)=2206$
$f_2(D,\{M,D\})=d(D,C)+d(C,N)=1730$
$f_2(M,\{M,C\})=2902$
$f_2(C,\{M,C\})=2480$
$f_2(D,\{D,C\})=2677$
$f_2(C,\{D,C\})=2731$

> no minimization for $f_2$ 
> DP is computationally lower than a Brute search

$f_1(C_0,L)=min_{J\&L}\{d(C_1,L)+f_2(J,L \cup (J))\}$ 
if $f_1(M,\{M\})=min_{J\in\{D,C\}}\{d(M,J)+f_2(J,\{M,J\})\}$ 
$=min(d(M,D)+f_2(D,\{M,D\}))$

$1343+2206=3549,921+2731=3552$ --> Minimum achieved at J = Miami



