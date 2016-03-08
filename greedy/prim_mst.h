// ../data/edges.txt

#ifndef StanfordAlgo2_prim_mst_h
#define StanfordAlgo2_prim_mst_h

#include <fstream>
#include <ios>
#include <vector>
#include <unordered_set>
#include <queue>
#include <algorithm>

using namespace std;

struct Edge
{
    int v1;
    int v2;
    int cost;
};

struct Vertex
{
    int node;
    vector<pair<int, int>> adjNodes;
};

class Graph
{
public:
    Graph(string filename)
    {
        ifstream fs(filename);
        if (fs.is_open()) {
            fs >> totalV >> totalE;
            for (int i = 1; i <= totalV; ++i) {
                graph.push_back(Vertex {i, vector<pair<int, int>> {}});
            }
            
            Edge e;
            while (fs >> e.v1 >> e.v2 >> e.cost) {
                graph[e.v1-1].adjNodes.emplace_back(e.v2, e.cost);
                graph[e.v2-1].adjNodes.emplace_back(e.v1, e.cost);
            }
        } else {
            cerr << "File open failed\n";
        }
    }
    
    void constructMST()
    {
        auto comp = [](const Edge &e1, const Edge &e2){return (e1.cost > e2.cost);};
        priority_queue<Edge, vector<Edge>, decltype(comp)> pq(comp);
        for (auto &adjNode : graph[0].adjNodes) {
            pq.push(Edge {1, adjNode.first, adjNode.second});
        }
        unordered_set<int> known {1};
        while (!pq.empty()) {
            Edge e = pq.top(); pq.pop();
            if (!known.count(e.v1) && known.count(e.v2))
                swap(e.v1, e.v2);
            
            if (known.count(e.v1) && !known.count(e.v2)) {
                known.insert(e.v2);
                mst.push_back(e);
                for (auto &adjNode : graph[e.v2-1].adjNodes) {
                    pq.push(Edge {e.v2, adjNode.first, adjNode.second});
                }
            }
            if (mst.size() >= totalV - 1)
                break;
        }
    }
    
    int totalCostsOfMST()
    {
        int sum = 0;
        for (auto edge = begin(mst); edge < end(mst); ++edge)
            sum += edge->cost;
        return sum;
    }
    
private:
    int totalV, totalE;
    vector<Vertex> graph;  // graph is an adjacent list, bunch of vertices
    vector<Edge> mst;  // mst is bunch of edges
};

#endif
