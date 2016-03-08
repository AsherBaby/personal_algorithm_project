#ifndef BinarySearchTree_BSTree_h
#define BinarySearchTree_BSTree_h

#include <iostream>
#include <string>
#include <queue>
#include <stack>

using namespace std;


// interface
template<typename Comparable>
class BinarySearchTree
{
private:
  struct BinaryNode
  {
    Comparable element;
    BinaryNode* left;
    BinaryNode* right;
    
    BinaryNode(const Comparable& x) : element{x},
    left{nullptr}, right{nullptr}
    {};
    
    BinaryNode( Comparable&& x) : element{x},
    left{nullptr}, right{nullptr}
    {};
    
  } *root;
  
public:
  BinarySearchTree() : root{nullptr} {}; // necessary
  BinarySearchTree(std::initializer_list<Comparable> c) : root{nullptr}
  {
    for (auto& it: c) insert(it);
  }
  // Big Five
  ~BinarySearchTree() {clear();}
  
  // need iterator to implement
  //BinarySearchTree(const BinarySearchTree& rhs);
  //BinarySearchTree(BinarySearchTree&& rhs);
  //BinarySearchTree& operator= (const BinarySearchTree& rhs);
  //BinarySearchTree& operator= (BinarySearchTree&& rhs);
  
  // iterator -- omitted
  
  // basic methods: empty, clear, size
  bool empty() const {return root == nullptr;}
  void clear()
  {
    clear(root);
    root = nullptr;
  }
  // int size();
  
  // specific methods:
  const Comparable& findMin() const
  {
    if (root == nullptr) throw "Empty tree";
    return findMin(root)->element;
  }
  const Comparable& findMax() const
  {
    if (root == nullptr) throw "Empty tree";
    return findMax(root)->element;
  }
  bool contains(const Comparable& x) const
  {
    if (root == nullptr) return false;
    return contains(x, root);
  }
  void printTree(std::ostream& out = std::cout) const
  {
    printTree(out, root);
    out << '\n';
  }
  
  void insert(const Comparable& x)
  {
    if (root == nullptr)
    {
      root = new BinaryNode {x};
      return;
    }
    insert(x, root);
  }
  void insert(Comparable&& x)
  {
    {
      if (root == nullptr)
      {
        root = new BinaryNode {x};
        return;
      }
      if (contains(x))
      {
        return;
      }
      insert(x, root);
    }
  }
  void remove(const Comparable& x)
  {
    if (root == nullptr) return; // if empty tree: no action
    if (!contains(x)) return; // if not find: no action
    remove(x, root);
  }
  
  // Leetcode
  bool inOrderCheck(BinaryNode* n, queue<int>& cell)
  {
    if (!n) return true;
    if (!inOrderCheck(n->left, cell)) return false;
    if (!(cell.front() < n->element)) return false;
    else
    {
      cell.pop();
      cell.push(n->element);
    }
    if (!inOrderCheck(n->right, cell)) return false;
    return true;
  }
  
  bool isValidBST() // in-order
  {
    if (!root) return true;
    queue<int> cell;
    cell.push(numeric_limits<int>::min());
    return inOrderCheck(root, cell);
  }
  //
  
private:
  void clear(BinaryNode* t)
  {
    if (t != nullptr)
    {
      clear(t->left);
      clear(t->right);
      delete t;
    }
  }
  
  BinaryNode* findMin(BinaryNode* t) const
  {
    if (t->left == nullptr) return t;
    else return findMin(t->left);
  }
  
  BinaryNode*& findRemoveMin(BinaryNode*& t) const
  {
    if (t->left == nullptr) return t;
    else return findRemoveMin(t->left);
  }
  
  BinaryNode* findMax(BinaryNode* t) const
  {
    if (t->right == nullptr) return t;
    else return findMax(t->right);
  }
  
  bool contains(const Comparable& x, BinaryNode* t) const
  {
    if (x == t->element)
    {
      return true;
    }
    else if (x < t->element)
    {
      if (t->left == nullptr) return false;
      else return contains(x, t->left);
    }
    else
    {
      if (t->right == nullptr) return false;
      else return contains(x, t->right);
    }
  }
  
  void printTree(std::ostream& out, BinaryNode* t) const
  {
    if (t == nullptr) return;
    printTree(out, t->left);
    out << t->element << ' ';
    printTree(out, t->right);
  }
  
  void insert(const Comparable& x, BinaryNode* t) // passing a pointer variable using call-by-reference
  {
    if (x < t->element)
    {
      if (t->left == nullptr)
      {
        t->left = new BinaryNode {x};
      }
      else
      {
        insert(x, t->left);
      }
    }
    else if (x > t->element)
    {
      if (t->right == nullptr)
      {
        t->right = new BinaryNode {x};
      }
      else
      {
        insert(x, t->right);
      }
    }
    else
    {
      ;
    }
  }
  
  void insert(Comparable&& x, BinaryNode* t)
  {
    if (x < t->element)
    {
      if (t->left == nullptr)
      {
        t->left = new BinaryNode {x};
      }
      else
      {
        insert(x, t->left);
      }
    }
    else if (x > t->element)
    {
      if (t->right == nullptr)
      {
        t->right = new BinaryNode {x};
      }
      else
      {
        insert(x, t->right);
      }
    }
    else
    {
      ;
    }
  }
  
  void remove(const Comparable& x, BinaryNode*& t)
  // remove() is tricky, and has x situations below
  // 1. removeNode is leaf: just remove it
  // 2. removeNode has one child: bypass and remove
  // 3. removeNode has two children: go right, findMin()
  {
    if (t == nullptr) return;
    if (x < t->element) remove(x, t->left);
    else if (x > t->element) remove(x, t->right);
    else
    {
      if (t->left != nullptr && t->right != nullptr) // two children
      {
        auto& tmp = findRemoveMin(t->right);
        t->element = tmp->element;
        delete tmp;
        tmp = nullptr;
      }
      else // no children or one child
      {
        auto tmp = t;
        t = t->left != nullptr ? t->left : t->right;
        delete tmp;
      }
    }
  }
};


#endif
