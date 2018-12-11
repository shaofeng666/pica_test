
# python 3 +selenium3 +HTMLTestRunner(优化本)

>框架使用python自带的unittest。ddt数据驱动；Excel管理测试用例、yaml管理测试页面元素，并对selenium API进行了封装，简化代码量同时记录log
###  bussinses 公共的逻辑模块编写
###  data 测试资源
 - case.xlsx 测试数据
 - page_data.yaml 页面对象数据

###  report存放测试报告
###  case存放测试用例。
###  log_doc 存放测试过程中的测试日志
###  suite  测试用例集
 - send_email.py 邮件发送模块
 - testsuite.py 测试用例集

### util 公共模块
 - gettestdata.py 获取测试数据模块
 - HTMLTestRunner_cn.py 美化后的报告模块（替代HTMLTestRunner）
 - log.py 日志模块
 - selse_feng.py 封装selenium方法

###  config.py 配置文件
###   run.py  执行脚本。

>**环境部署** 
- 在项目根目录下执行pip install -r requirements.txt  具体说明参考：https://www.jianshu.com/p/2cbc4fa7dbe3
- ddt驱动如果需要读**自定义测试用例名称**的名字需要修改ddt.py (数据驱动源码) 参考：https://www.jianshu.com/p/d1d22e6a655d

注意：如果ide导入模块失败，可以在命令行pip安装，命令如下
- 升级pip:   python -m pip install --upgrade pip(提示Could not find a version that satisfies the requirement yaml (from versions: )
No matching distribution found for yaml 时候使用)


