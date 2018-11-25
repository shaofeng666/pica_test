import yaml
from util import log
from config import root_path
from util.selse_feng import CreateDriver
import time


class Login_test:  # 登录模块封装
    def __init__(self, driver):
        # self.driver = CreateDriver("Chrome")
        self.driver = driver
        self.logs = log.log_message('登陆页面对象')
        self.file = open(root_path + "\\data\\page_data.yaml", "r", encoding="utf-8")
        self.data = yaml.load(self.file)
        self.file.close()
        self.host = self.data['basepage'].get('host')
        self.home_uri = self.data['login'].get('URI')
        self.ele_login_but = self.data['login'].get('ele_login_but')
        self.ele_name = self.data['login'].get('ele_name')
        self.ele_pwd = self.data['login'].get('ele_password')
        self.ele_sub = self.data['login'].get('ele_sub')
        self.ele_err_msg = self.data['login'].get('ele_err_msg')
        self.ele_succeed_msg = self.data['login'].get('ele_succeed_msg')

    def login(self, name, password, expect):
        self.logs.logger.info('调用login()')
        try:
            self.logs = log.log_message("登陆页面对象")
            self.driver.open(self.host + self.home_uri)
            self.driver.click_text(self.ele_login_but)
            # self.logs.logger.info('用户名:id为[%s]输入[%s]' % (self.ele_name, name))
            self.driver.send_key('id', self.ele_name, name)
            self.driver.send_key('id', self.ele_pwd, password)
            self.driver.click('xpath', self.ele_sub)
            time.sleep(5)
            if expect == 'true':
                self.login_su = self.driver.get_text('link_text', self.ele_succeed_msg)
                self.logs.logger.info('调用login()结束；返回%s' % self.login_su)
                return self.login_su
            elif expect == 'false':
                self.login_err = self.driver.get_text('xpath', self.ele_err_msg)
                self.logs.logger.info('调用login()结束；返回%s'%self.login_err)
                return self.login_err
            else:
                self.logs.logger.info('输入预期结果不在范围内！')

        except Exception as e:
            self.logs.logger.error('用例执行失败，原因：%s' % e)
            # finally:
            #     self.driver.quit()


if __name__ == '__main__':
    e = Login_test()
    # result=e.login('15928394929', 'qweqqq','false')
    result = e.login('u4272320562', '196847w', 'true')
    print(result)
