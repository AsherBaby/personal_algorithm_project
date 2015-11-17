#include "2sat.h"

int negate(int n, const int negationPoint);

bool twoSatScc(ImplicationGraph g)
{
    const int negationPoint = g.getNumVariables();
    auto sccs = scc_kosaraju(g);
    for (auto &scc : sccs) {
        for (int n : scc) {
            if (scc.count(negate(n, negationPoint))) {
                return false;
            }
        }
    }
    return true;
}

inline int negate(int n, const int negationPoint)
{
    return (n > negationPoint) ? n-negationPoint : n+negationPoint;
}