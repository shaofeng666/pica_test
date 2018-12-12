# coding:utf-8
from util.selse_feng import CreateDriver
import time
import requests
import json


def get_token():
    api_url = 'https://www.yunqueyi.com/web/registers/saasLogin?mobile=15607241351&OS=Win10&browser=Chrome&terminalType=PC&ipAddress=183.193.128.239&password=EABD8CE9404507AA8C22714D3F5EADA9&token=E7655872126845AC8F602898938552E3'
    try:
        res = requests.get(api_url)
        return json.dumps(res.json()['token'])
    except Exception as e:
        print('获取tuken失败，原因:[%s],接口返回码:[%s]' % (e, res.status_code))


driver = CreateDriver()
driver.open('https://www.yunqueyi.com')
driver.js('localStorage.setItem("token", %s);' % get_token())
print(get_token())
driver.f5()
time.sleep(2)
driver.click_text('健康管理')

time.sleep(5)
driver.quit()
# if __name__ == '__main__':
#     print(get_token())


# 通过cookie判断是否登陆:https://www.cnblogs.com/mengyu/p/7078561.html
# 通过localstorage绕过登陆:https://www.cnblogs.com/zanjiahaoge666/p/7576328.html