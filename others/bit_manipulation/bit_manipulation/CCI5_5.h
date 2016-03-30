
#ifndef CCI5_5_h
#define CCI5_5_h

bool powerOfTwo(int n) {
    if (n <= 0) return false;
    return ((n & (n-1)) == 0);
}

void test_of_CCI5_5() {
    assert(powerOfTwo(2) == true);
    assert(powerOfTwo(1024) == true);
    assert(powerOfTwo(1941204) == false);
}

#endif /* CCI5_5_h */
