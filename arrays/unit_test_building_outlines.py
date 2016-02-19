import unittest
from building_outlines import building_outlines

class Test(unittest.TestCase):

    def test_of_building_outlines(self):
        buildings = [[0, 3, 1], [1, 2, 2]]
        outlines = building_outlines(buildings)
        self.assertEqual(
            outlines,
            [[0, 1, 1], [1, 2, 2], [2, 3, 1]])

if __name__ == '__main__':
    unittest.main()
