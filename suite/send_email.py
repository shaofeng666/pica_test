#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from config import mail_host, mail_user, mail_pass, sender, to_addrs, mail_title, sender_nickname, to_addrs_nickname
import os

path = os.getcwd()
report_path = path + '\\report'
lists = os.listdir(report_path)  # 测试报告存放地址
lists.sort(key=lambda fn: os.path.getatime(report_path + '\\' + fn))  # 按时间顺序对该目录下的文件进行降序
last_report = os.path.join(report_path, lists[-1])  # 返回最新报告的完整路径


def send_email():
    '''
    配置邮箱参考：https://www.cnblogs.com/yufeihlf/p/5726619.html
    :return:
    '''

    # =============================
    # 配置邮件内容；
    # =============================
    f = open(last_report, 'rb')  # 以二进制方式读取文件
    mail_content = f.read()
    f.close()
    message = MIMEText(mail_content, 'html', 'utf-8')
    message['Subject'] = Header(mail_title, 'utf-8')  # 邮件标题
    message['From'] = Header(sender_nickname, 'utf-8')  # 发送者昵称
    message['To'] = Header(to_addrs_nickname, 'utf-8')  # 接收者昵称

    # =============================
    # 发送邮件配置
    # =============================
    try:
        smtpObj = smtplib.SMTP()  # 实例化SMTP()
        smtpObj.connect(mail_host, 25)  # mail_host 设置服务器；25 为 SMTP 默认端口号
        smtpObj.login(mail_user, mail_pass)  # mail_user 发件人用户名；mail_pass 发件人邮箱授权码
        smtpObj.sendmail(sender, to_addrs,
                         message.as_string())  # sender 发件人邮箱；to_addrs 邮件接收者地址。多个采用字符串列表['接收地址1','接收地址2','接收地址3',...]单个：'接收地址' ； message 发送的内容
        smtpObj.quit()  # 用于结束SMTP会话。
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
