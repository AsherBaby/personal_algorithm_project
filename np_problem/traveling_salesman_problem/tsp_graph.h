#ifndef StanfordAlgo2_tsp_graph_h
#define StanfordAlgo2_tsp_graph_h

#include <vector>
#include <string>
#include <iostream>
#include <fstream>

using std::vector;

class TspGraph
{
public:
    
    TspGraph() = default;
    
    void loadGraph(std::string filename)
    // for travelling salesman problem
    {
        std::fstream fs(filename);
        if (fs.is_open()) {
            fs >> nN;
            edges = vector<vector<float>> (nN+1, vector<float> (nN+1, 0));
            Node node;
            node.x = 0; node.y = 0;
            graph.push_back(node);
            while (fs >> node.x >> node.y) {
                graph.push_back(node);
            }
            for (int i=0; i <=nN; i++) {
                for (int j=0; j <= nN; j++) {
                    edges[i][j] = euclid(i, j);
                }
            }
        } else {
            std::cerr << "File open failed\n";
            exit(1);
        }
    }
    
    const int numNodes() const { return nN; }
    const int numEdges() const { return nE; }
    
    struct Node
    {
        float x;
        float y;
    };
    vector<Node> graph;
    vector<vector<float>> edges;
    
private:
    
    int nN;
    int nE;
    
    float euclid(int node, int adj)
    {
        float x1 = graph[node].x;
        float y1 = graph[node].y;
        float x2 = graph[adj].x;
        float y2 = graph[adj].y;
        return std::sqrt(std::pow(x1-x2,2)+std::pow(y1-y2,2));
    }
};

#endif
