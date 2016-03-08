#include <iostream>
#include <vector>

using namespace std;

void percolateDown(int hole, vector<int>& array, int size) // maxHeap
{
  int tmp = array[hole];
  int child;
  for (; hole*2+1 < size; hole = child)
  {
    child = hole * 2 + 1;  // left child
    if (child+1 < size && array[child] < array[child+1]) ++child; // right child
    if (tmp < array[child]) array[hole] = array[child];
    else break;
  }
  array[hole] = tmp;
}


void heapSort(vector<int>& array)
{
  for (int i = array.size()/2-1; i >= 0 ; --i)
  {
    percolateDown(i, array, array.size()); // build heap O(N)
  }
  for (int i = array.size()-1; i > 0; --i)
  {
    swap(array[0], array[i]);
    percolateDown(0, array, i);
  }
}


int main(int argc, const char * argv[])
{
  vector<int> array;
  for (int i = 0; i < 19; ++i) array.push_back(rand()%100);
  for (int number: array) cout << number << ' ';
  cout << "\n\n";
  heapSort(array); // handle duplicates !
  for (int number: array) cout << number << ' ';
  cout << endl;
  return 0;
}
