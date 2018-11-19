import unittest

from FizzBuzz import Fizz_Buzz

class Test_FizzBuzz(unittest.TestCase):
    def test_3と5両方の倍数の場合(self):
        self.assertEqual("FizzBuzz", Fizz_Buzz(15))

    def test_3の倍数の場合(self):
        self.assertEqual("Fizz", Fizz_Buzz(6))

    def test_5の倍数の場合(self):
        self.assertEqual("Buzz", Fizz_Buzz(10))



if __name__ == "__main__":
    unittest.main()


