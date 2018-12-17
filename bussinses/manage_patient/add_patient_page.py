# -*- coding: utf-8 -*-
# @Date    : 2018-12-15 20:48:37
# @Author  : Victor
from util.gettestdata import get_element
from util.selse_feng import CreateDriver
import random
from time import sleep



# 使用注释指定类型 参考：https://www.jetbrains.com/help/pycharm/type-hinting-in-product.html#adding-type-hints
class add_patient_obj():
    def __init__(self, driver: CreateDriver):
        self.driver = driver
        data = get_element('patient')
        self.ele_patient_menu = data.get('patient_menu')
        data = data['add_patient']
        self.ele_add_but = data.get('add_but')
        self.ele_moblie = data.get('mobile')
        self.ele_name = data.get('name')
        self.ele_confirm = data.get('btn_confirm')
        self.ele_cancel=data.get('btn_cancel')
        self.ele_succeed_msg = data.get('succeed_msg')
        self.ele_colse=data.get('colse')
    def add_patient(self, moblie, name, is_confirm,is_continue):
        driver = self.driver
        name=name+str(random.randint(0,1000))# 名字加上随机数，避免重复
        driver.click_text(self.ele_patient_menu)
        driver.click('xpath', self.ele_add_but)
        sleep(2)
        driver.clear_send_key('xpath', self.ele_moblie, moblie)
        driver.clear_send_key('xpath', self.ele_name, name)
        # 是否确认添加
        if is_confirm == '取消':
            driver.click('xpath',self.ele_cancel)
            sleep(2)
        elif is_confirm == '确认':
            driver.click('xpath', self.ele_confirm)
            msg = driver.get_text('xpath', self.ele_succeed_msg)
            assert msg == '添加成功！', '[%s]不等于:添加成功！' % msg
            # 添加成功是否继续？
            if is_continue=='关闭':
                driver.click('xpath',self.ele_colse)
        else:
            raise NameError('输入内容不在范围内;只能选择：取消、确认')