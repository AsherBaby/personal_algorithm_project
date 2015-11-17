// Bellman-Ford Algorithm
// single-source shortest path algorithm
// run on negative edges, can detect negative cycles
// DP, vars: dist, budgets
// O(mn)
// L(i, v) = min {
//     L(i-1, v);
//     for all edge(w,v) min {L(i-1, w) + c(w,v)};
// }
// where,
//     L: optimal (shortest) path length;
//     i: max number of edges permitted in path, range(0, n-1);
//     v: target node;
// This Bellman-Ford Algorithm is a push version, rather than request version

// data: ../data/g1.txt
//       ../data/g2.txt
//       ../data/g3.txt
//       ../data/large.txt

#ifndef StanfordAlgo2_bellmen_ford_h
#define StanfordAlgo2_bellmen_ford_h

#include <vector>
#include "graph.h"

using Dist = Graph::Dist;
using Node = Graph::Node;
using Edge = Graph::Edge;

std::vector<Dist> bellman_ford(int sID, Graph g);

#endif
