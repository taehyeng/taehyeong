
# -*- cording: utf-8 -*-
import unittest
import fizzbizz




class FizzBizz(unittest.TestCase):
    def setUp(self):
        print '\n'
        print "메소드를 실행합니다."

    def tearDown(self):
        print '\n'
        print "메소드를 모두 종료합니다."

    def test_fizzbizz(self):
        self.assertEqual(fizzbizz.fizzbizzf(3), "Fizz")
        self.assertEqual(fizzbizz.fizzbizzf(5), "Bizz")
        self.assertEqual(fizzbizz.fizzbizzf(15), "FizzBizz")
        try:
            self.assertEqual(fizzbizz.fizzbizzf(0), "ValueError")
        except AssertionError:
            print "ok"
if __name__=="__main__":
    unittest.main(verbosity=2)
