// Travelling salesman problem - dynamic programming solution
// for k = 1,2,3,...,n-1
//     for each subset S of size k (every node can be in S except node 1 (source))
//         for each i in S
//             L(S, i) = min(L(S-i, j) + Cji)
// return min(L({2,3,...,n},j) + Cj1)

#include <unordered_map>
#include <unordered_set>
#include <cstdint>
#include "tsp_dp.h"

using std::string;
using std::to_string;
using std::stoi;
using std::vector;
using std::unordered_map;
using std::pair;
using std::make_pair;
using std::numeric_limits;
using std::swap;

vector<uint32_t> generateKeys(int n, int end);
void generateKeys(int n, int start, int end, uint32_t &key,
                  vector<uint32_t> &keys);

int tsp_dp(TspGraph g)
{
    unordered_map<uint32_t, float> dpLast;
    unordered_map<uint32_t, float> dpNext;
    int nCities = g.numNodes();
    for (uint32_t key=2; key <= nCities; key++) {
        dpLast[key+(1<<(key+6))] = g.edges[1][key];
    }
    for (int k=2; k<nCities; k++) {
        std::cout << "Calculating size " << k << " now...\n";
        auto keys = generateKeys(k, nCities);
        for (const uint32_t key: keys) {
            for(int i=2; i<=nCities; i++) {
                if ((key>>(i+6))&1) { // if that city is visited
                    uint32_t newKey = key + i;
                    float len = numeric_limits<float>::max();
                    uint32_t newKey2 = key & ~(1<<(i+6));
                    for (int j=2; j<=nCities; j++) {
                        if ((newKey2>>(j+6))&1) { //
                            float trialLen = dpLast[newKey2+j] + g.edges[j][i];
                            if (trialLen < len) {
                                len = trialLen;
                            }
                        }
                    }
                    dpNext[newKey] = len;
                }
            }
        }
        std::cout << "    # old subsets: " << dpLast.size() << '\n';
        std::cout << "    # new subsets: " << dpNext.size() << '\n';
        swap(dpLast, dpNext);
        dpNext.clear();
    }
    float tspOpt = numeric_limits<float>::max();
    for (auto each: dpLast) {
        uint32_t key = each.first;
        float len = each.second;
        float trialOpt = len + g.edges[key&((1<<8)-1)][1];
        if (trialOpt < tspOpt) {
            tspOpt = trialOpt;
        }
    }
    return tspOpt;
}

// key: 24 bits for cities, 8 bits for destination city
vector<uint32_t> generateKeys(int n, int totalCities)
{
    uint32_t key = 0;
    vector<uint32_t> keys;
    generateKeys(n, 2, totalCities+1, key, keys);
    return keys;
}

void generateKeys(int n, int start, int end, uint32_t &key,
                  vector<uint32_t> &keys)
{
    if (n == 0) {
        keys.push_back(key);
        return;
    }
    for (int i=start; i<end; i++) {
        key |= 1<<(i+6);
        generateKeys(n-1, i+1, end, key, keys);
        key &= ~(1<<(i+6));
    }
}