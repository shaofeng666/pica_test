# -*- coding: utf-8 -*-
# @Date    : 2017-08-11 15:34:37
# @Author  : lileilei 
from suite.testsuite import create_report
from  suite import  testsuite
from suite.send_email import send_email

if __name__ == '__main__':
	# testsuite.run_case()
	testsuite.create_report('n')# 生成报告
	# send_email()# 发送邮件

