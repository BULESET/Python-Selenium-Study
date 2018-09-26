from Config11.driver import *
import os

class Loctor(driver11):
    def FindElenments(self,*loc):
        return self.driver.find_element(*loc)


    def inset_img(self):
        fun_path = os.path.dirname(__file__)
        print(fun_path)