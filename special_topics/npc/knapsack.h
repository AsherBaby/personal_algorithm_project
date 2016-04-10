// ../data/knapsack1.txt
// ../data/knapsack_big.txt

#ifndef StanfordAlgo2_knapsak_h
#define StanfordAlgo2_knapsak_h

#include <vector>
#include <string>
#include <fstream>

using namespace std;

struct Item
{
    int value;
    int weight;
};

class Knapsack
{
public:
    Knapsack(const string filename)
    {
        ifstream fs(filename);
        if (fs.is_open()) {
            fs >> totalSize >> numItems;
            Item i;
            items.push_back(i); // push back a dummy item
            while (fs >> i.value >> i.weight) {
                items.push_back(i);
            }
            fs.close();
        } else {
            cerr << "File open failed\n";
            exit(1);
        }
    }
    int getOptimal()
    {
        vector<int> dpTableOld (totalSize+1, 0);
        vector<int> dpTableNew (totalSize+1, 0);
        int i, w;
        for (i=1; i<=numItems; ++i) {
            cout << i << endl;
            for (w=1; w<=totalSize; ++w) {
                dpTableNew[w] = (w >= items[i].weight) ?
                max(dpTableOld[w],
                    dpTableOld[w-items[i].weight]+items[i].value) :
                dpTableOld[w];
            }
            swap(dpTableOld, dpTableNew);
        }
        return dpTableOld.back();
    }
    
private:
    int totalSize;
    int numItems;
    vector<Item> items;
};

#endif
