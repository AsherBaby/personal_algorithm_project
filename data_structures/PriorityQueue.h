#ifndef PriorityQueue_PriorityQueue_h
#define PriorityQueue_PriorityQueue_h

#include <string>

using namespace std;

template<typename Comparable>
class BinaryHeap
{
public:
  explicit BinaryHeap(int capacity = 100) : array(capacity+1), currentSize{0}
  {}
  
  explicit BinaryHeap(const vector<Comparable>& items) : array(items.size()+10),
    currentSize(items.size())
  {
    for (int i = 0; i < items.size(); ++i)
      array[i+1] = items[i];
    buildHeap();
  }
  
  // Big five -- omitted
  
  // Basics
  bool empty() const { return !currentSize; }
  void clear()
  {
    currentSize = 0;
    array.resize(100);
  }
  
  // Specific
  const Comparable& findMin() const { return array[1]; }
  void insert(const Comparable& x)
  {
    if (currentSize == array.size() - 1) array.resize(array.size()*2);
    array[0] = move(x);
    int hole = ++currentSize;
    for (; array[hole] < array[hole/2]; hole /= 2)
    {
      array[hole] = move(array[hole/2]);
    }
  }
  void insert(Comparable&& x);
  void deleteMin()
  {
    if (empty()) throw "Empty Binary Heap";
    array[1] = move(array[currentSize--]);
    percolateDown(1);
  }
  void deleteMin(Camparable& x)
  {
    if (empty()) throw "Empty Binary Heap";
    x = move(array[1]);
    array[1] = move(array[currentSize--]);
    percolateDown(1);
  }
  
private:
  int currentSize;
  vector<Comparable> array;
  
  void buildHeap()
  {
    for (int i = currentSize/2; i > 0; --i)
      percolateDown(i);
  }
  
  void percolateDown(int hole)
  {
    auto tmp = move(array[hole]);
    int child;
    for (; hole * 2 <= currentSize; hole = child) // while has child
    {
      child = hole * 2;
      if (child < currentSize && array[child] > array[child+1]) // find smaller child
        ++child;
      if (tmp > array[child])
        tmp = move(array[child]);
      else
        break;
    }
    array[hole] = move(tmp);
  }
};


#endif
