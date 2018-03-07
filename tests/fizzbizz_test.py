
# -*- coding: utf-8 -*-
import unittest
import fizzbizz




class FizzBizz(unittest.TestCase):
    def setUp(self):
        print '\n'
        print "�޼ҵ带 �����մϴ�."

    def tearDown(self):
        print '\n'
        print "�޼ҵ带 ��� �����մϴ�."

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
