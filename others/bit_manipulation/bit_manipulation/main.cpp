#include <iostream>
#include <cassert>
#include "CCI5-1.h"
#include "CCI5-2.h"
#include "CCI5-3.h"
#include "CCI5_4.h"
#include "CCI5_5.h"
#include "CCI5_6.h"

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
    test_of_CCI5_2();
    test_of_CCI5_3();
    test_of_CCI5_4();
    test_of_CCI5_5();
    test_of_CCI5_6();
    return 0;
}
