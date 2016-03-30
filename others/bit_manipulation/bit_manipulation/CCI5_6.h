

#ifndef CCI5_6_h
#define CCI5_6_h

#include <bitset>

using namespace std;

int conversion(int a, int b) {
    bitset<32> bs(a ^ b);
    return bs.count();
}

void test_of_CCI5_6() {
    assert(conversion(29, 15) == 2);
}

#endif /* CCI5_6_h */
