

#ifndef CCI5_8_h
#define CCI5_8_h

void drawLine(unsigned char screen[], int width, int x1, int x2, int y) {
    int start = y * width;
    int leftByteIdx = x1 / 8 + start;
    int rightByteIdx = x2 / 8 + start;
    int leftBitIdx = x1 % 8;
    int rightBitIdx = x2 % 8;
    unsigned char left = (1 << (8 - leftBitIdx)) - 1;
    screen[leftByteIdx] = left;
    unsigned char right = ~((1 << (8 - rightBitIdx - 1)) - 1);
    if (leftByteIdx == rightByteIdx) {
        screen[rightByteIdx] &= right;
        return;
    }
    screen[rightByteIdx] = right;
    unsigned char allOne = 0xff;
    for (int i = leftByteIdx+1; i < rightByteIdx; i++) {
        screen[i] = allOne;
    }
}

void test_of_CCI5_8() {
    unsigned char screen[12] = {};
    drawLine(screen, 4, 2, 7, 1);
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            cout << screen[i*4+j];
        }
        cout << endl;
    }
}


#endif /* CCI5_8_h */
