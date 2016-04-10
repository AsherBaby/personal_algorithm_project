#include "bellman-ford.h"

std::vector<Dist> bellman_ford(int sID, Graph g)
{
    std::vector<Dist> distances (g.numNodes()+1, Dist {});
    Dist &sourceDist = distances[sID];
    sourceDist.inf = false; sourceDist.n = 0; sourceDist.update = true;
    bool update = true;
    int i;
    for (i=0; i<=g.numNodes(); ++i) {
        if (!update)   // early stopping
            break;
        update = false;
        for (int v=0; v<=g.numNodes(); ++v) {
            if (distances[v].update) {
                distances[v].update = false;
                update = true;
                for (Edge &e : g.graph[v].edges) {
                    Dist &pushTarget = distances[e.to];
                    if (pushTarget.inf ||
                        pushTarget.n > distances[v].n + e.cost) {
                        pushTarget.n = distances[v].n + e.cost;
                        pushTarget.update = true;
                        pushTarget.inf = false;
                    }
                }
            }
        }
    }
    return (i < g.numNodes()) ? distances : std::vector<Dist> {};
}
