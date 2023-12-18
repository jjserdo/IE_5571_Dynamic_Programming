
#lecture 
September 18, 2023

---

- In $\epsilon$ - greedy we chose arms to random to encourage exploration
- can we get better performane by explaining in a more inlligent method
- choose actions according to their expected retun
- on stop t choose actio
$A_t\in(Q_t(a)+c\dqrt{logt/N_t(a)})$ 
c is a positive constn
N(a)= number of times we played with arm a
if not like this tehn greedy can jut c  = 0
- As N(a))