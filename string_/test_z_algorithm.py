import unittest
from .z_algorithm import *


class ZAlgorithmTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def testBuildZArray(self):
        self.assertEqual(buildZArray(""), [])
        self.assertEqual(buildZArray("a"), [0])
        self.assertEqual(buildZArray("aa"), [0, 1])
        self.assertEqual(buildZArray("aaaaa"), [0, 4, 3, 2, 1])
        self.assertEqual(buildZArray("aaabaab"), [0, 2, 1, 0, 2, 1, 0])
        self.assertEqual(buildZArray("abacaba"), [0, 0, 1, 0, 3, 0, 1])
        self.assertEqual(buildZArray("aabcaabxaaaz"), [
                         0, 1, 0, 0, 3, 1, 0, 0, 2, 2, 1, 0])

    def testIterAllMatches(self):
        self.assertEqual(list(iterAllMatches("", "x")), [])
        self.assertEqual(list(iterAllMatches("a word", "")), [])
        self.assertEqual(list(iterAllMatches("doodle", "de")), [])
        self.assertEqual(list(iterAllMatches("peter piper picked a peck of pickled peppers", "pe")), [0, 8, 21, 37, 40])
        self.assertEqual(list(iterAllMatches("apppa", "a")), [0, 4])
        
    def testCountMatches(self):
        self.assertEqual(countMatches("", "x"), 0)
        self.assertEqual(countMatches("a word", ""), 0)
        self.assertEqual(countMatches("doodle", "de"), 0)
        self.assertEqual(countMatches("peter piper picked a peck of pickled peppers", "pe"), 5)
        self.assertEqual(countMatches("apppa", "a"), 2)
        


if __name__ == '__main__':
    unittest.main()
