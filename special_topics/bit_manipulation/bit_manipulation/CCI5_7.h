
#ifndef CCI5_7_h
#define CCI5_7_h

int swapOddEvenBits(int num) {
    return ((num & 0xaaaaaaaa) >> 1) | ((num & 0x55555555) << 1);
}

void test_of_CCI5_7() {
    assert(swapOddEvenBits(0b10000110) == 0b01001001);
}

#endif /* CCI5_7_h */
