# encoding: utf-8  
""" 
@author: shaofeng wu
@file: config.py 
@time: 2018/11/9

"""
import  os
# =============
# 浏览器驱动 需要注意，如果浏览器启动后是空白页可能是驱动与浏览器版本不兼容
# 参考：https://www.jianshu.com/p/921e0cea40e7
# =============

# brower = 'Firefox'  # 测试所需要的浏览器
brower = 'Chrome'
# brower = 'ie'

# =============
# 测试报告参数
# =============
reporttitle = 'Python 自动化测试报告'  # 测试报告需要的title
description = '测试结果【截图+样式优化】'  # 测试报告需要的描述

# ==================
# 邮件参数
# ==================
# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "172212595@qq.com"  # 用户名
mail_pass = "ouiapsjgzjdvcaej"  # 授权码 qq邮箱获取地址：https://jingyan.baidu.com/article/6079ad0eb14aaa28fe86db5a.html
sender = '172212595@qq.com'  # 发送邮件的邮箱
to_addrs = ['172212595@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# 邮件内容
mail_title = 'Python 自动化测试报告'  # 邮件标题
sender_nickname = 'QQ个人邮箱'  # 发送人昵称
to_addrs_nickname = '某项目相关人员'  # 收件人昵称

root_path = os.path.split(os.path.realpath(__file__))[0]# 根目录
