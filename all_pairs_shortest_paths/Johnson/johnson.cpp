#include "johnson.h"

std::vector<std::vector<Dist>> johnson(Graph g)
{
    const std::vector<Dist> reweighting = bellman_ford(0, g);
    for (Node &n : g.graph) {
        for (Edge &e : n.edges) {
            e.cost += reweighting[e.from].n - reweighting[e.to].n;
        }
    }
    std::vector<std::vector<Dist>> ret;
    for (int i=0; i<=g.numNodes(); ++i) {
        ret.push_back(dijkstra(i, g));
        std::cout << "Processing " << i << "th node...\n";
    }
    for (int i=0; i<=g.numNodes(); ++i) {
        for (int j=0; j<=g.numNodes(); ++j) {
            if (!ret[i][j].inf)
                ret[i][j].n += reweighting[j].n - reweighting[i].n;
        }
    }
    std::cout << "Processing complete\n";
    return ret;
}
