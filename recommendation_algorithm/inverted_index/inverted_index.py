from collections import defaultdict
class Recommender:

    def __init__(self, n, m):
        self.user_table = [None] * (n+1)  # list or dict?
        self.inverted_table = [None] * (m+1)

    def find_similar_user(self, u_id, k):
        """Find top k similar users to u_id
        u1: m3, m1, m7
        u2: m5, m3
        u3: m3, m1, m9, m4
        becomes:
        m1: u1, u3
        m3: u1, u2, u3
        m4: u3
        m5: u2
        m7: u1
        m9: u3
        """
        similar_user = defaultdict(int)
        for m_id in self.user_table[u_id]:
            for u_id2 in self.inverted_table[m_id]:
                if u_id2 != u_id:
                    similar_user[u_id2] += 1
        return sorted(
            similar_user.keys(),
            key=similar_user.get,
            reverse=True)[:k]

    def build_inverted_table(self):
        for u_id in range(len(self.user_table)):
            if self.user_table[u_id]:  # can be None
                for m_id in self.user_table[u_id]:
                    if not self.inverted_table[m_id]:
                        self.inverted_table[m_id] = [u_id]
                    else:
                        self.inverted_table[m_id].append(u_id)
