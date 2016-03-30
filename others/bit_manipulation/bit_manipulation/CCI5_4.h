
#ifndef CCI5_4_h
#define CCI5_4_h

#include <bitset>

unsigned int nextNumber(unsigned int num) {
    bitset<32> bs(num);
    int i = 31;
    while (i >= 0 and bs[i]) i--;  // first 0
    while (i >= 0 and not bs[i]) i--;  // first 1 with 0 ahead
    if (i == -1) return num;
    bitset<32> ng = bs;
    swap(ng[i+1], ng[i]);
    int l = i-1;
    int r = 0;
    while (l > r) {
        while (l > r and ng[l] == 0) l--;
        while (l > r and ng[r] == 1) r++;
        swap(ng[l], ng[r]);
    }
    return ng.to_ulong();
}

void test_of_CCI5_4() {
    assert(nextNumber(1) == 2);
    assert(nextNumber(12) == 17);
}

#endif /* CCI5_4_h */
