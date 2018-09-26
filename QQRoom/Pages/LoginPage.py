from  selenium.webdriver.common.by import By
from  Config11.driver import driver11
from Config11.Locators import Loctor
from  time import  sleep

class LoginPage(Loctor):

    username = (By.ID,"u")
    password = (By.ID,"p")
    LoginButten = (By.ID,"login_button")
    ForgetPasswordButten =(By.ID,"forgetpwd")
    QQLoginButten = (By.CLASS_NAME,"img_out_focus")
    UsenameAndPasswordLoginButten = (By.ID,"switcher_plogin")
    SignUpNewCountButten = (By.LINK_TEXT,"注册新账号")
    SuggestionsButten = (By.ID,"feedback_qlogin")
    ZhuYE = (By.LINK_TEXT,"个人中心")
    Cloas = (By.ID,"dialog_button_1")

    def CheclElenments(self):
        self.FindElenments(*self.Cloas).click()
        self.FindElenments(*self.ZhuYE)
        return self.FindElenments(*self.ZhuYE).text


    def LoginPage(self):
        self.driver.switch_to.frame("login_frame")
        self.FindElenments(*self.UsenameAndPasswordLoginButten).click()

    def InputUsename(self):
        self.driver.switch_to.frame("login_frame")
        self.FindElenments(*self.username).clear()
        self.FindElenments(*self.username).send_keys("")

    def InputPassword(self):
        self.driver.switch_to.frame("login_frame")
        self.FindElenments(*self.password).clear()
        self.FindElenments(*self.password).send_keys("")

    def ClickLoginButten(self):
        self.driver.switch_to.frame("login_frame")
        self.FindElenments(*self.LoginButten).click()

    def QQLoginButten1(self):
        self.driver.switch_to.frame("login_frame")
        self.FindElenments(*self.QQLoginButten).click()
        self.driver.switch_to.parent_frame()


class LoginBuessnessED(LoginPage,driver11):

    def LoginBuessness(self):
        sleep(3)
        self.QQLoginButten1()
        sleep(3)
        self.CheclElenments()
        # sleep(3)
        # self.InputUsename()
        # sleep(3)
        # self.InputPassword()
        # sleep(3)
        # self.ClickLoginButten()
