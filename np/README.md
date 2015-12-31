
---
### Traveling Salesman Problem (TSP)
Traveling Salesman Problem is slightly explored here. A DP solution
with O ( n^2 * 2^n ) is developed just to taste the hardness of a
NP-Complete problem.

---
### 2-SAT Problem
Example of 2-SAT problem:

Input: (x1 v x2) ^ (~x1 v x2) ^ (x3 v x4) ^ (~x2 v ~x4)

Output: True if exists an assignment that simultaneously satisfies
every clause, False otherwise.

Solution: reduction to computing Strongly Connected Components, and
solved in linear time.


---
### More topics...
