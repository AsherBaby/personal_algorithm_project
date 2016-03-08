#include "catch.hpp"
#include "BSTree.h"

TEST_CASE("Testing binary search tree class")
{
  // setup()
  BinarySearchTree<int> tree {3,5,2,4,1,6};
  
  SECTION("Tesing constructor with initializer list")
  {
    REQUIRE(tree.findMin() == 1);
    REQUIRE(tree.findMax() == 6);
  }
  
  SECTION("Tesing clear() and empty()")
  {
    REQUIRE(tree.empty() == false);
    tree.clear();
    REQUIRE(tree.empty() == true);
  }
  
  SECTION("Tesing contains()")
  {
    REQUIRE(tree.contains(4) == true);
    REQUIRE(tree.contains(7) == false);
  }
  
  SECTION("Tesing insert()")
  {
    tree.insert(7);
    REQUIRE(tree.findMax() == 7);
  }
  
  SECTION("Testing remove()")
  {
    tree.remove(2);
    REQUIRE(tree.findMin() == 1);
    tree.remove(1);
    REQUIRE(tree.findMin() == 3);
    tree.remove(7);
    REQUIRE(tree.findMin() == 3);
    tree.remove(5);
    REQUIRE(tree.findMax() == 6);
  }
  
  SECTION("Testing binary search tree validation (leetcode) ")
  {
    tree.clear();
    tree.insert(1);
    REQUIRE(tree.isValidBST() == true);
  }

}

