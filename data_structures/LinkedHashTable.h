#ifndef HashTable_LinkedHashTable_h
#define HashTable_LinkedHashTable_h

#include <vector>
#include <list>

using namespace std;

template<typename HashedObj>
class HashTable
{
public:
  // constructor
  explicit HashTable(int size = 101)
  {
    int i = 0;
    while (i < size)
    {
      theLists.push_back(list<HashedObj> {});
      ++i;
    }
  }
  
  // basics
  bool contains(const HashedObj& x) const
  {
    auto& whichList = theLists[myhash(x)];
    return find(begin(whichList), end(whichList), x) != end(whichList);
  }
  void clear();
  
  // more
  bool insert(const HashedObj& x)
  {
    return false;
  }
  bool insert(HashedObj&& x)
  {
    auto& whichList = theLists[myhash(x)];
    if (find(begin(whichList), end(whichList), x) == end(whichList))
    {
      whichList.push_front(move(x));
      // rehash()
      return true;
    }
    else
    {
      return false;
    }
  }
  bool remove(const HashedObj& x)
  {
    auto& whichList = theLists[myhash(x)];
    auto theObject = find(begin(whichList), end(whichList), x);
    if (theObject != end(whichList))
    {
      whichList.erase(theObject);
      return true;
    }
    else
    {
      return false;
    }
  }

  
private:
  vector<list<HashedObj>> theLists;
  int currentSize;
  void rehash();
  size_t myhash(const HashedObj& x) const
  {
    static hash<HashedObj> hf;
    return hf(x) % theLists.size();
  }
  
};

#endif
