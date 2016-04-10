#ifndef CCI5_1_h
#define CCI5_1_h

int insert(int N, int M, int j, int i) {
    int mask = ~((1 << (j+1)) - (1 << i));
    N &= mask;
    M <<= i;
    return N | M;
}

void test_of_CCI5_1() {
    int N = 0b10000000000;
    int M = 0b10011;
    assert(insert(N, M, 6, 2)==0b10001001100);
}

#endif /* CCI5_1_h */
