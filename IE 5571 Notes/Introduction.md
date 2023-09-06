September 6, 2023
#lecture

---

## Notes
- DP and RL
- solve the same problems but DP might solve the exact solution
- RL for Artificial Intelligence
##### **RL**: A set of tools for approximate control of stochastic processes
	good enough not the best
	random
	- tools for approximate dynamic programming
#### Reinforcement learning has *two traditions*
##### 1. Learning by trial and error
	- historical, like animals or babies
	- Learning by trial and error goes back to 19th century psychologists
		- learning sports seems more like trial and error: reward and consequence
		- need a bit of guidance when learning complex things
		- for more complex, need to be a bit smarter when training an agent
		- as much as possible, decrease human intervention
			- twisting hips too early
			- punish early to improve learning: don't go towards the hole
	- Alan Turing in mid 1948 hypothesized that we could train automata using pleasure/pain signals
	- AI practitioners in 1950s and 1960s studied learning by trial and error
		- stalled out in 1970s because wasn't working but got back in 1980s and 1990s
##### 2. Optimal control and the dynamic programming principle
-- Mathematical framework, space navigation
-- Optimal control and dynamic programming are usually credited to Richard Bellman
-- George Dansic: learning programming, Richard called it dynamic cuz it sounds cooler
-- Use dynamic programming principle to establish the [[Bellman Equation]]
-- In principle can solve Bellman Equation to identify optimal policies/control
-- Some downsides to this approach
	1. computational complexity grows exponentially in problem size
	2.  requires knowledge of the exact model of dynamical system
		-- Atari games doesn't have a clear model or game playing cuz no model how a random stranger 

Connections between AI and optimal control were established in 1989 by Chris Watkins with [[Q-factors]]

#### Success of RL
-- In 1982 John Tessauro developed TD-Gammon using RL techniques
	-- performed close to top human level
	-- learned by self play
-- AlphaGo first AI to beat top human at Go in 2015 and trained using RL
	-- training initialized by supervised learning of human play
-- AlphaZero trained to play Go with only RL which is just self play
	-- surpassed AlphaGo
-- chatGPT a Large Language Model (LLM) that predicts next word
	-- what made it successful is Reinforcement learning with Human Feedback (RLHF)
> You need to be rich to do this so that's why it's mostly American

	




---

## Comments
- Homeworks and Final Project/Presentation Only
- No Exams