
# -*- coding: utf-8 -*-
import unittest
import nun




class TAX(unittest.TestCase):
    def setUp(self):
        print '\n'
        print "�޼ҵ带 �����մϴ�."

    def tearDown(self):
        print '\n'
        print "�޼ҵ带 ��� �����մϴ�."

    def test_yoonnun(self):
        self.assertEqual(nun.yoonnun(2000), u"����")
        self.assertEqual(nun.yoonnun(1900), u"���")
        self.assertEqual(nun.yoonnun(1992), u"����")
        self.assertEqual(nun.yoonnun(1989), u"���")
         

if __name__=="__main__":
    unittest.main(verbosity=2)

