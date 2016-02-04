// Strong connected components
// Kosaraju's algorithm
// 2 DFS

#ifndef StanfordAlgo2_scc_h
#define StanfordAlgo2_scc_h

#include <vector>
#include <unordered_set>
#include "scc_graph.h"

using std::vector;
using std::unordered_set;

vector<unordered_set<int>> scc_kosaraju(SCCGraph g);

#endif

// Example:
// SCCGraph g;
// g.loadGraph("/Users/Pei/Projects/Self-C++/StanfordAlgo2/data/SCC.txt");
// auto sccs = scc_kosaraju(g);
