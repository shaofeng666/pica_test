# -*- coding: utf-8 -*-
# @Date    : 2018-12-15 20:48:37
# @Author  : Victor
from util.gettestdata import get_element
from util.selse_feng import CreateDriver
import random
import string
from time import sleep
from util import log


# 使用注释指定类型 参考：https://www.jetbrains.com/help/pycharm/type-hinting-in-product.html#adding-type-hints
class add_patient_obj():
    def __init__(self, driver: CreateDriver, log: log):
        self.driver = driver
        self.logs = log
        data = get_element('patient')
        self.ele_patient_menu = data.get('patient_menu')
        data = data['add_patient']
        self.ele_add_but = data.get('add_but')
        self.ele_moblie = data.get('mobile')
        self.ele_name = data.get('name')
        self.ele_confirm = data.get('btn_confirm')
        self.ele_cancel = data.get('btn_cancel')
        self.ele_succeed_msg = data.get('succeed_msg')
        self.ele_colse = data.get('colse')
        self.ele_continue_add = data.get('continue_add')
        self.ele_add_info=data.get('add_info')
        self.ele_add_address=data.get('add_address')

    def add_patient(self, moblie, name, is_confirm, is_continue,address):
        driver = self.driver
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        print(name)
        self.name = name + ran_str  # 名字加上随机字符串，避免重复
        driver.click_text(self.ele_patient_menu)
        sleep(1)
        # driver.click('xpath', self.ele_add_but) # 元素被挡住，selenium 的click不能用
        driver.js("document.getElementsByClassName('btn btn-big')[0].click()")
        sleep(1)
        driver.clear_send_key('xpath', self.ele_moblie, moblie)
        driver.clear_send_key('xpath', self.ele_name, self.name)
        # 是否确认添加
        if is_confirm == '取消':
            driver.click('xpath', self.ele_cancel)
            sleep(2)
            self.logs.logger.info('取消')
        elif is_confirm == '确定':
            driver.click('xpath', self.ele_confirm)
            msg = driver.get_text('xpath', self.ele_succeed_msg)
            assert msg == '添加成功！', '[%s]不等于:添加成功！' % msg
            self.logs.logger.info('->确定：%s' % msg)
            # 添加成功是否继续？
            self.logs.logger.info('添加居民成功；是否继续添加：%s' % is_continue)
            if is_continue == '关闭浏览器':
                self.logs.logger.info('关闭浏览器')
            elif is_continue == '关闭':
                driver.click('xpath', self.ele_colse)
                self.logs.logger.info('关闭弹层')
            elif is_continue == '继续添加居民':
                self.logs.logger.info('继续添加居民')
                self.driver.click('xpath', self.ele_continue_add)
                driver.clear_send_key('xpath', self.ele_moblie, moblie)
                driver.clear_send_key('xpath', self.ele_name, ran_str)
                driver.click('xpath', self.ele_confirm)
                msg = driver.get_text('xpath', self.ele_succeed_msg)
                assert msg == '添加成功！', '[%s]不等于:添加成功！' % msg
                self.logs.logger.info('->确定：%s' % msg)
            elif is_continue == '继续完善资料':
                self.driver.click('id',self.ele_add_info)
                sleep(2)
                # self.driver.send_key('xpath',self.ele_add_address,address) # 页面无法加载
                self.logs.logger.info('继续完善资料')
            else:
                raise NameError('is_continue只能选择："关闭浏览器","关闭","继续添加居民","继续完善资料"')
        else:
            raise NameError('is_confirm只能选择：取消、确定')
