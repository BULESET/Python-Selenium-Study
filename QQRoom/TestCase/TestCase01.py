import unittest
from Pages import LoginPage
from Config11.Report import *

class TestCase01(unittest.TestCase):
    def setUp(self):
        print("测试开始")

    def test_login(self):
        title = LoginPage.LoginBuessnessED()
        title.GetTestUrl()
        title.QQLoginButten1()
        self.assertEqual(title.CheclElenments(),"个人中心")

    def tearDown(self):
        print("测试结束")

if __name__ == "__mian":
    suite = unittest.TestSuite()
    loder= suite.addTest(TestCase01("test_login"))
    ruuner = unittest.TextTestRunner()
    b = ruuner.run(suite)
    a = TR(b)
