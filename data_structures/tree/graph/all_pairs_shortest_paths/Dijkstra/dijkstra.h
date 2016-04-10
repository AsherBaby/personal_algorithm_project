// Dijkstra algorithm
// attr: greddy, single-source shortest path algorithm
// attr: cannot handle negative edge
// time: O(mlgn)

// data: ../data/g1.txt
//       ../data/g2.txt
//       ../data/g3.txt
//       ../data/large.txt

#ifndef StanfordAlgo2_dijkstra_h
#define StanfordAlgo2_dijkstra_h

#include <vector>
#include <queue>
#include "graph.h"

using Dist = Graph::Dist;
using Node = Graph::Node;
using Edge = Graph::Edge;

std::vector<Dist> dijkstra(int sID, Graph g);
// compute the shortest paths lengths from s to each node in g
// input: source node s, graph g
// output: a list of distances from s to each node in graph g

#endif