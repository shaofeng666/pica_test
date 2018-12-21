# -*- coding: utf-8 -*-
# @Date    : 2018-12-15 20:48:37
# @Author  : Victor
from util.gettestdata import get_element
from util.selse_feng import CreateDriver
import random
from time import sleep



# 使用注释指定类型 参考：https://www.jetbrains.com/help/pycharm/type-hinting-in-product.html#adding-type-hints
class del_patient_obj():
    def __init__(self, driver: CreateDriver):
        self.driver=driver
        data=get_element('patient')
        self.ele_patient_menu=data.get('patient_menu')
        data=data['del_patient']
        self.ele_seek_patient=data.get('seek_patient')
        self.ele_seek_btn=data.get('seek_btn')
        self.ele_batch_del=data.get('batch_del')
        self.ele_confirm=data.get('btn_confirm')
        self.ele_cancel=data.get('btn_cancel')

    def del_patient(self,moblie,is_confirm,imgs):
        driver=self.driver
        driver.click_text(self.ele_patient_menu)
        sleep(2)
        driver.clear_send_key('xpath',self.ele_seek_patient,moblie)
        driver.click('xpath',self.ele_seek_btn)
        # driver.click('xpath',self.ele_check) # 元素被挡住，selenium 的click不能用
        driver.js("document.getElementsByClassName('svg-icon ng-scope')[1].click()")
        driver.js('window.scrollTo(100,500)')
        driver.click('xpath',self.ele_batch_del)
        if is_confirm=='确定':
            confirm_msg=driver.get_text('xpath',self.ele_confirm)
            driver.click('xpath', self.ele_confirm)
            sleep(0.5)
            imgs.append(self.driver.add_img())
            return confirm_msg
        elif is_confirm=='取消':
            cancel_msg=driver.get_text('xpath',self.ele_cancel)
            driver.click('xpath',self.ele_cancel)
            sleep(0.5)
            imgs.append(self.driver.add_img())
            return cancel_msg
        else:
            raise NameError('输入内容不在范围内;只能选择：取消、确认')