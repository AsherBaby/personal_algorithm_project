#include <iostream>
#include <vector>

using namespace std;

class Sort
{
public:
  
  void quickSort(vector<int>& array)
  {
    quickSort(array, 0, array.size());
  }
  
  void insertionSort(vector<int>& array, int begin, int end)
  {
    for (int i = 1; i < end; ++i)
    {
      int tmp = array[i];
      int j = i;
      for (; j > 0 && tmp < array[j-1]; --j)
      {
        array[j] = array[j-1];
      }
      array[j] = tmp;
    }
  }
  
  void quickSort(vector<int>& array, int begin, int end)
  {
    if (begin + 10 < end)
    {
      int m = median(array, begin, end);
      int l = begin;
      int r = end-2;
      while(1)
      {
        while (array[++l] < m) {};
        while (array[--r] > m) {};
        if (l < r)
        {
          swap(array[l], array[r]);
        }
        else
        {
          break;
        }
      }
      swap(array[l], array[end-2]);
      quickSort(array, begin, l);
      quickSort(array, l+1, end);
    }
    else
    {
      insertionSort(array, begin, end);
    }
  }
  
  int median(vector<int>& array, int begin, int end)
  {
    int m = (begin+end)/2;
    if (array[begin] > array[m]) swap(array[begin], array[m]);
    if (array[begin] > array[end-1]) swap(array[begin], array[end-1]);
    if (array[m] > array[end-1]) swap(array[m], array[end-1]);
    swap(array[m], array[end-2]);
    return array[end-2];
  }
};
int main(int argc, const char * argv[])
{
  Sort sort;
  vector<int> array;
  for (int i = 0; i < 39; ++i) array.push_back(rand()%100);
  sort.quickSort(array);
  for (int n: array) cout << n << ' ';
  cout << '\n';
  return 0;
}
