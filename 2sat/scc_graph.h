#ifndef StanfordAlgo2_scc_graph_h
#define StanfordAlgo2_scc_graph_h

#include <vector>
#include <string>
#include <fstream>
#include <iostream>

using std::vector;

class SCCGraph
{
public:
    
    SCCGraph() : numNodes{0} {};
    
    virtual void loadGraph(std::string filename)
    {
        std::fstream fs;
        fs.open(filename);
        if (fs.is_open()) {
            vector<Edge> edges;
            Edge e;
            while (fs >> e.from >> e.to) {
                edges.push_back(e);
                if (e.from > numNodes) {
                    numNodes = e.from;
                }
                if (e.to > numNodes) {
                    numNodes = e.to;
                }
            }
            // read file complete ...
            
            graph = vector<Node> (numNodes+1, Node {});
            for (Edge &e: edges) {
                graph[e.from].outedges.push_back(e);
                graph[e.to].inedges.push_back(e);
            }
        } else {
            std::cerr << "File open failed\n";
            exit(1);
        }
    }
    
    void refresh()
    {
        for (auto &node : graph) {
            node.visited = false;
            node.processed = false;
        }
    }
    
    struct Edge {
        int from;
        int to;
    };
    
    struct Node {
        bool visited;
        bool processed;
        vector<Edge> outedges;
        vector<Edge> inedges;
        Node() : visited{false}, processed{false} {};
    };
    
    int numNodes;
    vector<Node> graph;
};
#endif
