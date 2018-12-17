# coding:utf-8
from util.selse_feng import CreateDriver
import requests
import json
from util import log
from util.gettestdata import get_element


def storage_login(driver):
    '''
    通过localStorage 绕过登陆
    参考：# 通过cookie判断是否登陆:https://www.cnblogs.com/mengyu/p/7078561.html
    # 通过localstorage绕过登陆:https://www.cnblogs.com/zanjiahaoge666/p/7576328.html
    :param driver: 浏览器驱动
    :return: 
    '''
    try:
        data = get_element('login')
        ele_succend_but = data.get('ele_succend_but')
        ele_succeed_msg = data.get('ele_succeed_msg')

        driver.open('https://www.yunqueyi.com')  # 打开首页
        is_login = driver.get_text('xpath', '//*[@id="login"]/li[1]/span')
        logs = log.log_message('登陆测试')
        if is_login == '登录':  # 判断如果页面有'登录'按钮则证明没有登录，向local Storage中添加token、name、doctorId
            api_url = 'https://www.yunqueyi.com/web/registers/saasLogin?mobile=15607241351&OS=Win10&browser=Chrome&terminalType=PC&ipAddress=183.193.128.239&password=EABD8CE9404507AA8C22714D3F5EADA9&token=E7655872126845AC8F602898938552E3'
            r = requests.get(api_url)
            driver.js('localStorage.setItem("token", %s);' % json.dumps(r.json()['token']))
            driver.js('localStorage.setItem("user_name", %s);' % json.dumps(r.json()['picapDoctor']['name']))
            driver.js('localStorage.setItem("doctorId", %s);' % json.dumps(r.json()['picapDoctor']['id']))
            logs.logger.info('页面未登陆;向localStorage中插入：token、user_name、doctorId')
        else:  # 如果页面没有"登陆"则证明已登录
            logs.logger.info('页面已登陆;')
        driver.f5()
        driver.move_element('id', ele_succend_but)
        login_su_msg = driver.get_text('link_text', ele_succeed_msg)
        assert login_su_msg == '个人资料',  '[%s]不等于[个人资料]'%login_su_msg
    except AssertionError as e:  # 明确抛出此异常
        print('登陆失败：[assert except]:%s ' % e)


if __name__ == '__main__':
    # 验证是否登陆成功
    imgs=[]
    driver = CreateDriver(imgs)
    storage_login(driver)
    driver.click_text('健康管理')
    driver.quit()
