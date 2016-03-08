//
//  list.cpp
//  DoubleLinkedLIst
//
//  Created by Asher on 11/30/14.
//  Copyright (c) 2014 Asher. All rights reserved.
//

#include <stdio.h>
#include "list.h"


// Use of uninitialized pointers can crash programs, so initialize them.
List::List() : head{nullptr}, tail{nullptr}
{
  ;
}

void List::insert(int x)
{
  if (head == nullptr)
  {
    Node* first = new Node {x, nullptr, nullptr};
    head = first;
    tail = first;
  }
  else
  {
    Node* node = new Node {x, nullptr, tail};
    tail->next = node;
    tail = tail->next;
  }
}

void List::print()
{
  for (Node* node = head; node != nullptr;)
  {
    printf("%d ", node->element);
    node = node->next;
  }
}

