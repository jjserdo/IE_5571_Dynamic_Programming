
September 18, 2023
#knowledge #lecture 

---

[[Lecture 4 Notes]]
- So far all algorithms has been based on maintaining using estimates of q*(a)
- In GBH, we build prefernces for eah arm, H_t(a)
- P(A_t=a)=pi_t(a)

---

[[Gradient Ascent]]
Our goal is to maximize $E(R_t)$
$$E(R_t)=\sum^{k}_{a=1} \pi_{t(a)} q_*(a)$$
but we don't know $q_*(a)$
If we were to maximize $E(R_t)$ via gradient ascent we would update $H_t(a)$ via
$$H_{t+1}(a) = H_{t(a)}+\alpha\frac{\partial}{\partial H_t(a)}E(R_t)$$
{}