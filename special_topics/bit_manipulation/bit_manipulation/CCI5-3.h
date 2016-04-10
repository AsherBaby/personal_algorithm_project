/*
 This problem can be extended to flip M bits to gain the longest sequence of 1s.
 */
#ifndef CCI5_3_h
#define CCI5_3_h

#include <string>
#include <vector>
#include <bitset>

using namespace std;

int flipToWin(int num) {
    bitset<32> bs(num);
    int dp0 = bs[0];
    int dp1 = 1;
    int maxL = 1;
    for (int i = 1; i < 32; i++) {
        if (bs[i] == 0) {
            dp1 = dp0 + 1;
            dp0 = 0;
        } else {
            dp1 += 1;
            dp0 += 1;
        }
        maxL = max(maxL, dp1);
    }
    return maxL;
}

void test_of_CCI5_3() {
    assert(flipToWin(1775) == 8);
    assert(flipToWin(6) == 3);
    assert(flipToWin(-1) == 32);
}

#endif /* CCI5_3_h */
