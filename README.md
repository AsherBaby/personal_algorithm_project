## Pei Zhao's personal algorithm projects

---
### Inversion Count of Two Arrays
Inversion count of two arrays implemented with Divide and Conquer
algorithm, with O(n log(n)) time complexity.

Example:

    A = [1, 3, 2]
    B = [2, 3, 1]
    #inv is 3.

The smaller #inv, the more similar of the two arrays.

This algorithm can be used for recommendation system.


---
### Graph Connectivity
#### Compute Connected Components in Undirected Graph
In undirected graph, connected components can be easily computed
through a BFS-loop or DFS-loop, or using a Union & Find data structure.

And the running time is O( m+n )

#### Compute Weak Connected Components in Directed Graph
In directed graph, the weak connected components can be computed
by leveraging union & find data structure.

Union & Find data structure with path compression is coded in less than
20 lines, with two APIs:

1. union(a, b)
2. find(a)  -> root_a

Union & Find is a very compact but useful data structure for many
applications.

#### Compute Strong Connected Components in Directed Graph
Computing strong connected components is slightly harder than the
above problems.
[Kosaraju Two-Pass Algorithm](https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm)
is implemented here. This algorithm firstly magically compute an order
of nodes from a reverse graph. Then it uses simple DFS-loop based on
this order to compute SCC.

The running time of this algorithm is O( m+n ).

---
### Dijkstra Shortest Path Algorithm with Hash Heap Data Structure
Dijkstra greedy algorithm for computing shortest path in non-negative
edge graph is explored. For maximum performance of Dijkstra algorithm,
Hash Heap data structure is meticulously coded and exhausted tested
for use.

Hash Heap data structure has the following API with complete
O( log(n) ) running time for each operation:

1. add(node)
2. poll() -> min node
3. update(node)
4. delete(node)

With the help of hash heap, the Dijkstra algorithm has running time of
O( m log(n) ).

---
### All Pairs Shortest Paths (w/o test cases)
All pairs shortest paths problem can be considered as upgrade of the
single source shortest path problem. Two well-known algorithms for
single source shortest path problem:

1. Dijkstra Algorithm: non-negative edge, O( m log(n) )
2. Bellman-Ford Algorithm: O( mn )

For the all pairs shortest paths problem, there are also two mature  
algorithms:

1. Floyd-Warshall Algorithm: O ( n^3 ), a DP algorithm
2. Johnson's Algorithm: O( mn log(n) )

Worthy of mentioning is that, Johnson's algorithm beat Floyd-Warshall
algorithm for sparse graph. For dense graph, I personally recommend
Floyd-Warshall algorithm, because it is extremely easy to code, if
the state function is being understood, just three loops.

---
### Traveling Salesman Problem (TSP)

Traveling Salesman Problem is slightly explored here. A DP solution
with O ( n^2 * 2^n ) is developed just to taste the hardness of a
NP-Complete problem.

---
### More topics...
