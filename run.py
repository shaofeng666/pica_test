# -*- coding: utf-8 -*-
# @Date    : 2018-08-11 15:34:37
# @Author  : Victor
from suite.testsuite import create_report
from  suite import  testsuite
from suite.send_email import send_email

if __name__ == '__main__':
	# testsuite.run_case()# 调试、不生成报告
	# testsuite.run_this_case('n',pitent)#调试 运行指定.py文件 生成报告
	testsuite.create_report('n')# 生成报告
	# send_email()# 发送邮件



