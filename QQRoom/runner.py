import unittest
import time
from HTMLTestRunner import HTMLTestRunner
from Pages import LoginPage
import logging
from Config11.Log import Logger


class TestCase01(unittest.TestCase):
    def setUp(self):
        self.logger = Logger("ceshi")
        self.logger.logger.debug("测试开始")



    def test_login(self):

        self.logger.logger.debug("打开浏览器")
        self.title = LoginPage.LoginBuessnessED()
        self.logger.logger.warning("输入测试地址")
        self.title.GetTestUrl()
        self.logger.logger.error("登录")
        self.title.QQLoginButten1()
        self.logger.logger.error("检查是否登录成功")
        self.assertEqual(self.title.CheclElenments(),"个人中心")

    def tearDown(self):
        print("测试结束")

if __name__== "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestCase01("test_login"))
    report_dir = r'E:\Python_script\Selenium_study\Auto_Test_Script_Study\QQRoom\TestReport'
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    repordername = report_dir + "/" + now + "-result.html"
    '''创建文件的正确方法是：open（路径+文件名字+文件格式）'''
    with open(repordername, "wb") as f:
        runer = HTMLTestRunner(stream=f, title="Test Report", description="Testcasesult")
        runer.run(suite)
        f.close()