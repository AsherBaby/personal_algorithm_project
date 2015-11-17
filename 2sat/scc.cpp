#include "scc.h"
#include <stack>

using std::stack;

vector<int> dfsloop1(SCCGraph &g);
vector<unordered_set<int>> dfsloop2(SCCGraph &g, const vector<int> &magicOrder);
void dfs1(SCCGraph &g, int leader, vector<int> &finishT);
void dfs2(SCCGraph &g, int leader, unordered_set<int> &scc);

vector<unordered_set<int>> scc_kosaraju(SCCGraph g)
{
    auto finishT = dfsloop1(g);
    g.refresh(); // reset visited and processed status for every node
    auto sccs = dfsloop2(g, finishT);
    return sccs;
}

vector<int> dfsloop1(SCCGraph &g)
{
    vector<int> finishT;
    for (int i=1; i<=g.numNodes; i++) {
        if (!g.graph[i].visited) {
            dfs1(g, i, finishT);
        }
    }
    return finishT;
}

void dfs1(SCCGraph &g, int leader, vector<int> &finishT)
// iterative dfs postorder
{
    stack<int> funStack;
    stack<int> userStack;
    funStack.push(leader);
    while (!funStack.empty()) {
        int n = funStack.top();
        auto &node = g.graph[n];
        if (node.visited) {
            if (!node.processed) {
                finishT.push_back(n);
                node.processed = true;
            }
            funStack.pop();
        } else {
            node.visited = true;
            for (auto &edge : node.inedges) {
                auto &adj = g.graph[edge.from];
                if (!adj.visited) {
                    userStack.push(edge.from);
                }
            }
            if (userStack.empty()) {
                // postorder processing
                finishT.push_back(n);
                node.processed = true;
                funStack.pop();
            } else {
                while (!userStack.empty()) {
                    funStack.push(userStack.top()); userStack.pop();
                }
            }
        }
    }
}

vector<unordered_set<int>> dfsloop2(SCCGraph &g, const vector<int> &magicOrder)
{
    vector<unordered_set<int>> sccs;
    for (auto i=magicOrder.rbegin(); i<magicOrder.rend(); i++) {
        if (!g.graph[*i].visited) {
            unordered_set<int> scc;
            dfs2(g, *i, scc);
            sccs.push_back(move(scc));
        }
    }
    return sccs;
}


void dfs2(SCCGraph &g, int leader, unordered_set<int> &scc)
// iterative DFS preorder
{
    stack<int> funStack;
    funStack.push(leader);
    while (!funStack.empty()) {
        int n = funStack.top(); funStack.pop();
        auto &node = g.graph[n];
        if (!node.visited) {
            node.visited = true;
            scc.insert(n);
            for (auto &edge : node.outedges) {
                auto &adj = g.graph[edge.to];
                if (!adj.visited) {
                    funStack.push(edge.to);
                }
            }
        }
    }
}