# -*- coding: utf-8 -*-
# @Date    : 2018-08-11 15:34:37
# @Author  : Victor
from suite.testsuite import create_report
from suite.send_email import send_email
from  suite import  testsuite
from suite import run_case
# 运行指定文件中的测试类
from case.manage_patient import test_add_patient

if __name__ == '__main__':
    # 调试、不生成报告
	# testsuite.run_case()

    # 调试 运行指定.py文件中的类 生成报告
	run_case.run_this_case('n',test_add_patient.add_patient)

    # 生成报告
	# testsuite.create_report('n')

    # 发送邮件
	# send_email()



