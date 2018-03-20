# coding:utf-8
#这里写了一个登录博客园的类，登录博客园方法
class Login_Blog():
    """登录类封装"""
    def __init__(self,driver):
        """初始化driver参数"""
        self.driver=driver
    def input_user(self,username):
        """输入用户名"""
        self.driver.find_element_by_id("input1").clear()
        self.driver.find_element_by_id("input1").send_keys(username)
    def input_psw(self,psw):
        """输入密码"""
        self.driver.find_element_by_id("input2").clear()
        self.driver.find_element_by_id("input1").send_keys(psw)
    def click_button(self):
        """点击登录按钮"""
        self.driver.find_element_by_id("signin").click()
    def login(self,username,psw):
        """登录公告方法"""
        self.input_user(username)
        self.input_psw(psw)
        self.click_button()

