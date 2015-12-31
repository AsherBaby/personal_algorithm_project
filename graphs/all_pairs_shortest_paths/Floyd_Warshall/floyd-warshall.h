// Floyd-Warshall Algorithm
// O(n3), can compete with Johnson's Algorithm in dense graph
// DP
// L(s,t,k) = min {
//     L(s,t,k-1);
//     L(s,k,k-1) + L(k,t,k-1);
// }
// where, s: source node, t: target node,
//        k: only use node Id less equal than k in path

// data: ../data/g1.txt
//       ../data/g2.txt
//       ../data/g3.txt
//       ../data/large.txt

#ifndef StanfordAlgo2_floyd_warshall_h
#define StanfordAlgo2_floyd_warshall_h

#include <vector>
#include "graph.h"

using Dist = Graph::Dist;
using Node = Graph::Node;
using Edge = Graph::Edge;

std::vector<std::vector<Dist>> floyd_warshall(Graph g);

#endif
