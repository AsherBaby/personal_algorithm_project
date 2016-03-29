

#ifndef CCI5_2_h
#define CCI5_2_h
#include <string>

using namespace std;

string doubleToBinary(double num) {
    string ans = "";
    for (int i = 0; i < 32; i++) {
        num *= 2;
        if (num >= 1) {
            ans.push_back('1');
            num -= 1;
            if (num == 0) {
                return ans;
            }
        } else {
            ans.push_back('0');
        }
    }
    return "ERROR";
}

void test_of_CCI5_2() {
    assert(doubleToBinary(0.25)=="01");
    assert(doubleToBinary(0.72)=="ERROR");
}

#endif /* CCI5_2_h */
