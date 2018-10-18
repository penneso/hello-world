import unittest
import fuzzy_percentiles

class TestFuzzyPercentiles(unittest.TestCase):

    def test_find_balance(self):
        self.assertEqual(fuzzy_percentiles.find_balance([1, 3], 14, 5), 80)

    def test_find_tot_balance(self):
        self.assertEqual(fuzzy_percentiles.find_tot_balance([[1,3],[4,4,4,4,4],[5,8],[9,9,10],[13,15]],14), 96)

    def test_fill_bins(self):

        bins=fuzzy_percentiles.fill_bins([1, 3, 8, 15, 9, 13, 4, 4, 9, 5, 4, 4, 10, 4], 5)

        #test no empty bins
        self.assertEqual(len(bins), 5)

        #test score order preserved
        self.assertEqual(bins[0] + bins[1] + bins[2] + bins[3] + bins[4], [1, 3, 4, 4, 4, 4, 4, 5, 8, 9, 9, 10, 13, 15])

        #test same score is in the same bin
        for x in range(len(bins)):
            for y in range(len(bins)):
                if x != y:
                    self.assertFalse(set(bins[x]) & set(bins[y]))

if __name__ == '__main__':
    unittest.main()
