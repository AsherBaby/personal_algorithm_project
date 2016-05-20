class MedianOfTwoSortedArray {
public:
    /**
     * @param A: An integer array.
     * @param B: An integer array.
     * @return: a double whose format is *.5 or *.0
     */
    static double findMedianSortedArrays(vector<int> A, vector<int> B) {
        int total = A.size() + B.size();

        if (total % 2 == 1) {
            return (double)find(A, 0, B, 0, total/2);
        } else {
            return (find(A, 0, B, 0, total/2-1) + find(A, 0, B, 0, total/2)) / 2.0;
        }
    }

    static double find(vector<int>& A, int AStart, vector<int>& B, int BStart, int k) {
        if (AStart >= A.size()) {
            return B[k];
        }
        if (BStart >= B.size()) {
            return A[k];
        }
        if (k == 0) {
            return min(A[AStart], B[BStart]);
        }

        if (k/2+AStart >= A.size()) {  // A is too short
            return find(A, AStart, B, BStart+(k+1)/2, k-(k+1)/2);
        }

        if (k/2+BStart >= B.size()) {
            return find(A, AStart+(k+1)/2, B, BStart, k-(k+1)/2);
        }

        if (A[k/2+AStart] < B[k/2+BStart]) {
            return find(A, AStart+(k+1)/2, B, BStart, k-(k+1)/2);
        } else {
            return find(A, AStart, B, BStart+(k+1)/2, k-(k+1)/2);
        }
    }
};
