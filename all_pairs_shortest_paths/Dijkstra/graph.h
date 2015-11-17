#ifndef StanfordAlgo2_graph_h
#define StanfordAlgo2_graph_h

#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <cmath>

using std::vector;

class Graph
{
public:
    
    Graph() = default;
    
    virtual void loadGraph(std::string filename)
    // for Dijkstra, Bellman-Ford, Johnson, Floyd-Warshall
    {
        std::fstream fs(filename);
        if (fs.is_open()) {
            fs >> nN >> nE;
            for (int i=0; i<=nN; ++i) {
                // the 0th node is the extra source node,
                // which would benefit Johnson's algorithm
                graph.emplace_back(i);
            }
            for (int i=1; i<=nN; ++i) {
                // node 0 points to every other node in graph
                graph[0].edges.emplace_back(0,i,0);
            }
            Edge e {0, 0, 0};
            while (fs >> e.from >> e.to >> e.cost) {
                graph[e.from].edges.push_back(e);
            }
        } else {
            std::cerr << "File open failed\n";
            exit(1);
        }
    }
    
    struct Dist
    {
        bool inf;
        bool update; // init with false, used by Bellman-Ford
        int n;
        Dist() { inf = true; update = false; };
    };

    struct Edge
    {
        int from;
        int to;
        int cost;
        Edge(int from, int to, int cost) : from(from), to(to), cost(cost) {};
    };

    struct Node
    {
        int nodeID;
        Dist dist;
        bool known;  // init with false, used by Dijkstra
        std::vector<Edge> edges;
        Node(int nodeID) : nodeID(nodeID), known(false) {};
    };
    
    const int numNodes() const { return nN; }
    const int numEdges() const { return nE; }
    
    vector<Node> graph;
    
private:
    
    int nN;
    int nE;
    
};

#endif
