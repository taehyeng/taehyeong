
# -*- cording: utf-8 -*-
import unittest
import tax




class TAX(unittest.TestCase):
    def setUp(self):
        print '\n'
        print "메소드를 실행합니다."

    def tearDown(self):
        print '\n'
        print "메소드를 모두 종료합니다."

    def test_tex(self):
        self.assertEqual(tax.tex(16,30000,"children"), 13500)
        self.assertEqual(tax.tex(16,30000,"nochildren"), 5400)
        self.assertEqual(tax.tex(16,10000,"children"), 5000)
        self.assertEqual(tax.tex(16,10000,"nochildren"), 2000)
        try:
            self.assertEqual(tax.tex(16,30000,"children"), 0)
        except:
            pass
if __name__=="__main__":
    unittest.main(verbosity=2)

