from util import log
from util.gettestdata import get_element
from time import sleep
from util.selse_feng import CreateDriver


class Login_test:  # 登录模块封装
    def __init__(self, driver:CreateDriver):
        # self.driver = CreateDriver("Chrome")
        self.driver = driver
        self.logs = log.log_message('登陆页面对象')
        self.host = get_element('basepage').get('host')
        login_data=get_element('login')
        self.home_uri = login_data.get('URI')
        self.ele_login_but = login_data.get('ele_login_but')
        self.ele_name = login_data.get('ele_name')
        self.ele_pwd = login_data.get('ele_password')
        self.ele_sub = login_data.get('ele_sub')
        self.ele_name_err_msg = login_data.get('ele_name_err_msg')
        self.ele_pwd_err_msg = login_data.get('ele_pwd_err_msg')
        self.ele_succend_but=login_data.get('ele_succend_but')
        self.ele_succeed_msg = login_data.get('ele_succeed_msg')

    def login(self, name, password, expect):
        self.logs.logger.info('调用login()')
        self.logs = log.log_message("登陆页面对象")
        self.driver.open(self.host + self.home_uri)
        self.driver.make_maxwindow()
        self.driver.click('xpath', self.ele_login_but)
        self.driver.send_key('name', self.ele_name, name)
        self.driver.send_key('xpath', self.ele_pwd, password)
        sleep(1)
        self.driver.click('xpath', self.ele_sub)
        if expect == 'name_err':
            self.login_name_err_msg = self.driver.get_text('xpath', self.ele_name_err_msg)
            self.logs.logger.info('调用login()结束；return:[%s]' % self.login_name_err_msg)
            return self.login_name_err_msg
        elif expect == 'pwd_err':
            self.login_pwd_err_msg = self.driver.get_text('xpath', self.ele_pwd_err_msg)
            self.logs.logger.info('调用login()结束；return:[%s]' % self.login_pwd_err_msg)
            return self.login_pwd_err_msg
        elif expect == 'succeed':
            sleep(2)
            self.driver.move_element('id',self.ele_succend_but)
            self.login_su_msg = self.driver.get_text('link_text', self.ele_succeed_msg)
            self.logs.logger.info('调用login()结束；return:[%s]' % self.login_su_msg)
            return self.login_su_msg
        else:
            self.logs.logger.info('输入预期结果不在范围内！')



