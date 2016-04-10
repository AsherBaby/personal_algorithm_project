// L(s,t,k) = min {
//     L(s,t,k-1);
//     L(s,k,k-1) + L(k,t,k-1);
// }
//
// Super space optimization:
// L(s,t,k) = min {
//     L(s,t,k);
//     L(s,k,k) + L(k,t,k)
// }
// Why the second recurrence function is correct?
// Only if L(s,t,k) <= L(s,t,k-1) is always correct.

#include "floyd-warshall.h"

std::vector<std::vector<Dist>> floyd_warshall(Graph g)
{
    std::vector<std::vector<Dist>> dp (g.numNodes()+1,
         std::vector<Dist> (g.numNodes()+1, Dist {}));
    for (int i=0; i<=g.numNodes(); i++) {
        Dist &d = dp[i][i];
        d.inf = false;
        d.n = 0;
    }
    for (Node &n : g.graph) {
        for (Edge &e: n.edges) {
            Dist &d = dp[e.from][e.to];
            d.inf = false;
            d.n = e.cost;
        }
    }
    for (int k=0; k<=g.numNodes(); k++) {
        std::cout << "At " << k << "th iteration...\n";
        for (int s=0; s<=g.numNodes(); s++) {
            for (int t=0; t<=g.numNodes(); t++) {
                if (!dp[s][k].inf && !dp[k][t].inf) {
                    if (dp[s][t].inf) {
                        dp[s][t].inf = false;
                        dp[s][t].n = dp[s][k].n + dp[k][t].n;
                    } else {
                        if (dp[s][t].n > dp[s][k].n + dp[k][t].n) {
                            dp[s][t].n = dp[s][k].n + dp[k][t].n;
                        }
                    }
                }
            }
        }
    }
    std::cout << "Processing complete.\n";
    return dp;
}