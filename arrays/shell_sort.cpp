#include <iostream>
#include <vector>
#include <unordered_set>
#include <ctime>

using namespace std;


void shellSort(vector<int>& array)
{
  int hk = 1;
  while (hk < (array.size()+1)/2) hk *= 2;
  hk -= 1;  // hk = pow(2, k) - 1
  for (int gap = hk; gap > 0; gap = (gap+1)/2-1) // hk = 1, 3, 7, ...
  {
    for (int i = gap; i < array.size(); ++i)
    {
      int tmp = array[i];
      int j = i;
      for (; j >= gap && tmp < array[j-gap]; j -= gap) array[j] = array[j-gap];
      array[j] = tmp;
    }
  }
}

int main(int argc, const char * argv[])
{
  int size = 5000000;
  unordered_set<int> hashTable;
  for (int i = 0; i < size; ++i) hashTable.insert(rand());
  vector<int> array;
  for (int number: hashTable) array.push_back(number);
  
  shellSort(array);
  
  return 0;
}
