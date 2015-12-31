#include "dijkstra.h"

int bfs(int sID, Graph g);
std::vector<Graph::Dist> dijkstra(int sID, Graph g)
// compute the shortest paths lengths from s to each node in g
// input: source node id sID, graph g
// output: a list of distances from s to each node in graph g
{
    Node &s = g.graph[sID];
    s.dist.n = 0; s.dist.inf = false;
    int knownSize = 0;
    auto cmp = [](const Node &n1, const Node &n2) {
        return n1.dist.n > n2.dist.n;  // min-heap
    };
    std::priority_queue<Node, std::vector<Node>, decltype(cmp)> unknown(cmp);
    unknown.push(s);
    int numReachableNodes = bfs(sID, g);
    while (knownSize < numReachableNodes) {
        int nID = unknown.top().nodeID; unknown.pop();
        Node &n = g.graph[nID];
        if (!n.known) {
            n.known = true;
            ++knownSize;
            for (Edge &e : n.edges) {
                Node &adj = g.graph[e.to];
                if (!adj.known) {
                    if (adj.dist.inf || adj.dist.n > n.dist.n + e.cost) {
                        adj.dist.inf = false;
                        adj.dist.n = n.dist.n + e.cost;
                        unknown.push(adj);
                    }
                }
            }
        }
    }
    std::vector<Dist> ret;
    for (Node &n : g.graph) {
        ret.push_back(n.dist);
    }
    return ret;
}

int bfs(int sID, Graph g)
// bfs O(m)
// input: source node id sID, graph g
// output: number of nodes that are reachable from sID, including sID itself
{
    Node &n = g.graph[sID];
    n.known = true;
    int numReadchableNodes = 1;
    std::queue<int> q;
    q.push(sID);
    while (!q.empty()) {
        int nID = q.front(); q.pop();
        Node &n = g.graph[nID];
        for (Edge &e : n.edges) {
            int adjID = e.to;
            Node &adjNode = g.graph[adjID];
            if (!adjNode.known) {
                adjNode.known = true;
                q.push(adjID);
                ++numReadchableNodes;
            }
        }
    }
    return numReadchableNodes;
}