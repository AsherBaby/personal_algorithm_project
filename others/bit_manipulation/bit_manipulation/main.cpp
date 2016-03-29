#include <iostream>
#include <cassert>
#include "CCI5-1.h"

using namespace std;

// getBit
bool getBit(int num, int i) {
    return ((num & (1 << i)) != 0);
}

// setBit
int setBit(int num, int i) {
    return num | (1 << i);
}

// clearBit
int clearBit(int num, int i) {
    return num & (~(1 << i));
}

// updateBit
int updateBit(int num, int i, int value) {
    return (num & (~(1 << i))) | (value << i);
}

int main(int argc, const char * argv[]) {
    test_of_CCI5_1();
    return 0;
}
