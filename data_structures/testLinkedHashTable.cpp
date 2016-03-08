#include "catch.hpp"
#include "LinkedHashTable.h"
#include <string>

using namespace std;

TEST_CASE("Testing hash tabe class")
{
  // setup()
  HashTable<string> dict;
  
  SECTION("Tesing contain and insert method")
  {
    REQUIRE(dict.contains("apple") == false);
    bool insert = dict.insert("apple");
    REQUIRE(insert == true);
    REQUIRE(dict.contains("apple") == true);
    insert = dict.insert("apple");
    REQUIRE(insert == false);
  }
  
  SECTION("Testing remove method")
  {
    bool remove = dict.remove("apple");
    REQUIRE(remove == false);
    dict.insert("apple");
    string a = "apple";
    remove = dict.remove("apple");
    REQUIRE(remove == true);
  }
  
}
