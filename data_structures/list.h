#ifndef DoubleLinkedLIst_list_h
#define DoubleLinkedLIst_list_h

class List
{
public:
  List();
  void insert(int x);
  void remove(int location);
  void print();
  
private:
  struct Node
  {
    int element;
    Node* next;
    Node* last;
  };
  Node* head;
  Node* tail;
};

#endif
