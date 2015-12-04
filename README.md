## Pei Zhao's personal algorithm projects

This project contains Recommendation Algorithms, Graph Connectivity,
Dijkstra with Hash Heap, All Pairs Shortest Paths, TSP, 2-SAT,
Backtracking, Multithreading/Multiprocessing, Tiny URL, Rate Limiter,
Bloomfilter, and MapReduce.

---
### Recommendation related Algorithms
Inversion Count of Two Arrays

Inversion count of two arrays implemented with Divide and Conquer
algorithm, with O(n log(n)) time complexity.

Example:

    A = [1, 3, 2]
    B = [2, 3, 1]
    #inv is 3.

The smaller #inv, the more similar of the two arrays.

This algorithm can be used for recommendation system.

Inverted Index

For a content-based recommendation algorithm, suppose there are m
movies, n users. The basic algorithm takes O( n(m^2) ) running time
to find the most similar user for one user. Using inverted index,
the running time can be optimized to O ( nm ).

---
### Graph Connectivity
Compute Connected Components in Undirected Graph

In undirected graph, connected components can be easily computed
through a BFS-loop or DFS-loop, or using a Union & Find data structure.

And the running time is O( m+n )

Compute Weak Connected Components in Directed Graph

In directed graph, the weak connected components can be computed
by leveraging union & find data structure.

Union & Find data structure with path compression is coded in less than
20 lines, with two APIs:

1. union(a, b)
2. find(a)  -> root_a

Union & Find is a very compact but useful data structure for many
applications.

Compute Strong Connected Components in Directed Graph

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
### 2-SAT Problem
Example of 2-SAT problem:

Input: (x1 v x2) ^ (~x1 v x2) ^ (x3 v x4) ^ (~x2 v ~x4)

Output: True if exists an assignment that simultaneously satisfies
every clause, False otherwise.

Solution: reduction to computing Strongly Connected Components, and
solved in linear time.

---
### Backtracking
Backtracking is simply DFS with some strategy to stop searching
deeper, so that without searching the whole tree, solutions could be
found quicker than exhausted search.

Backtracking is usually used when a solution could be found recursively.

Some common problems solved by backtracking are:

1. N Queen
2. Word Search
3. Palindrome Partitioning
4. Number of Islands

---
### Multithreading, Multiprocessing
Condition variable and semaphore are explored here, a thread-safe
consumer-producer class is implemented.

---
### Tiny URL
Primary key + Map + [0-9a-zA-Z]

Use primary key as tiny url (address).
Map (Dictionary) stores mapping between long url and short url, and
quickly find already exists long url.
[0-9a-zA-Z] uses 62 symbols to make tiny url shorter.


---
### Rate Limiter
Three different rate limiter algorithms are implemented:

1. Gap
2. Bucket
3. Queue

And each pros and cons are analyzed.


---
### Bloomfilter
A static size bloomfilter is implemented with bitarray and hash.

API:

1. insert()
2. lookup()

Bloomfilter has relative small false positive depends on how full it is.


---
### MapReduce
Problems of word count, inverted index, anagrams, top ten are solved
using MapReduce

---
### More topics...
