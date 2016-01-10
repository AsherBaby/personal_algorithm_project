from key_indexed_counting import key_indexed_counting

def radix_sort(a):
    for i in range(len(a)-1, -1, -1):
        key_indexed_counting(a, key=lambda x: x[i])

    
