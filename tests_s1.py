import unittest
import simple1

class TestSimple(unittest.TestCase):

    def test_numbers(self):
        inputs=(2,3)
        res=simple1.add_square(2,3)
        self.assertEqual(res,25)

    def test_numbers_new(self):
        inputs=(2,5)
        res=simple1.add_square(2,5)
        self.assertEqual(res,25)

if __name__=='__main__':
    unittest.main()
