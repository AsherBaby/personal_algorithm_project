// Travelling salesman problem - dynamic programming solution
// Travelling salesman problem : NP-Complete
// The solution is inspired by Bellman-Ford algorithm
// O(N*N*2toN)
// DP solution is never practcal for travelling salesman problem in real world.
//     It would be obviously slow when n > 20. Some slick methods, such as local
//     search, greedy approximation...
// This solution can handle 25 cities at most for modern computers, while brute
//     force way allow computer handle 12 at most.

#ifndef __StanfordAlgo2__tsp_dp__
#define __StanfordAlgo2__tsp_dp__

#include "tsp_graph.h"

using Node = TspGraph::Node;

int tsp_dp(TspGraph g);

#endif /* defined(__StanfordAlgo2__tsp_dp__) */
