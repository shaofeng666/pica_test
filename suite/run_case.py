# -*- coding: utf-8 -*-
# @Date    : 2018-08-18 00:01:37
# @Author  : Victor
import time
import unittest
from config import description, reporttitle
from util.modules.HTMLTestRunner_cn import HTMLTestRunner
from config import root_path


def run_this_case(is_new,test_class):
    '''
    根据指定规则运行对应测试类，并生成报告
    :param is_new: n 覆盖旧的报告，y 根据时间格式生产新报告
    :param test_class: 需要被运行的测试类，规则：文件名.类名 
    :return: 
    '''
    test_suit = unittest.TestSuite()
    # 运行指定模块下方法
    test_suit.addTest(unittest.makeSuite(test_class))

    now = time.strftime('%Y-%m-%d_%H_%M', time.localtime(time.time()))
    # 如果是 y 报告名称插入时间，每次新增；如果是 n 每次生成的报告名称相同,会覆盖前一个报告
    if is_new == 'y':
        report_dir = root_path + '\\report\\%s.html' % now
    elif is_new == 'n':
        report_dir = root_path + '\\report\\HTMLtemplate.html'
    else:
        raise NameError('输入内容不在范围内;只能选择：n、y')
    re_open = open(report_dir, 'wb')
    runner = HTMLTestRunner(stream=re_open, title=reporttitle, description=description)
    runner.run(test_suit)
    re_open.close()
