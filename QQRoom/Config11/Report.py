import time
from HTMLTestRunner import HTMLTestRunner
import  os


def Report(suit):
    report_dir = r'E:\Python_script\Selenium_study\Auto_Test_Script_Study\QQRoom\TestReport'
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    repordername = report_dir + "/" + now + "-result.html"
    '''创建文件的正确方法是：open（路径+文件名字+文件格式）'''
    with open(repordername, "wb") as f:
        runer = HTMLTestRunner(stream=f, title="Test Report", description="Testcasesult")
        runer.run(suit)
        f.close()



func_path=os.path.dirname(__file__)
fun = os.getcwd()