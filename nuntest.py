
# -*- cording: utf-8 -*-
import unittest
import nun




class TAX(unittest.TestCase):
    def setUp(self):
        print '\n'
        print "메소드를 실행합니다."

    def tearDown(self):
        print '\n'
        print "메소드를 모두 종료합니다."

    def test_yoonnun(self):
        self.assertEqual(nun.yoonnun(2000), u"윤년")
        self.assertEqual(nun.yoonnun(1900), u"평년")
        self.assertEqual(nun.yoonnun(1992), u"윤년")
        self.assertEqual(nun.yoonnun(1989), u"몰라")
         

if __name__=="__main__":
    unittest.main(verbosity=2)

