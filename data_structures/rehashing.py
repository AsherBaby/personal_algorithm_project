def rehashing(self, in_ht):
    n = len(in_ht)
    cap = 2 * n  # !
    out_ht = [None] * cap
    for node in in_ht:
        while node:  # !
            this = node
            node = node.next
            hashcode = this.val % cap
            dest = out_ht[hashcode]
            this.next = dest
            out_ht[hashcode] = this
    return out_ht
