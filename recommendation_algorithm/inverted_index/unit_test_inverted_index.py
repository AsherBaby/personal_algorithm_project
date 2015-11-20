import unittest
from inverted_index import Recommender

class TestRecommenderWithInvertedIndex(unittest.TestCase):

    def setUp(self):
        """
        u1: m3, m1, m7
        u2: m5, m3
        u3: m3, m1, m9, m4
        """
        self.recommender = Recommender(3, 9)  # 3 users, 9 movies
        self.recommender.user_table[1] = [3, 1, 7]
        self.recommender.user_table[2] = [5, 3]
        self.recommender.user_table[3] = [3, 1, 9, 4]

    def test_of_find_similar_user(self):
        self.recommender.build_inverted_table()
        self.assertEqual(
            self.recommender.find_similar_user(1, 2), [3, 2])

if __name__ == '__main__':
    unittest.main()
