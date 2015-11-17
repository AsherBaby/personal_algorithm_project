// Johnson's algorithm
// Used for sparse graph, and probably in dense graph too
// it is a hack..
// reweighting
// Johnson's algorithm = 1x Bellman-Ford + Nx Dijkstra
// O(mnlogn) blazing fast!
// Another hack is add extra single source, pointing to each node in graph, and
//     keep itself invisible from the whole graph. That's hacking!

// data: ../data/g1.txt
//       ../data/g2.txt
//       ../data/g3.txt
//       ../data/large.txt

#ifndef StanfordAlgo2_johnson_h
#define StanfordAlgo2_johnson_h

#include "dijkstra.h"
#include "bellman-ford.h"

std::vector<std::vector<Dist>> johnson(Graph g);

#endif
