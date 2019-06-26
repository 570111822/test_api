#-*- coding:utf-8 -*
'''多文件用例：test1.py,test2.py生成HTML报告
在目录下必须要新建一个：__init__.py的空文件
'''
import time
from HTMLTestRunner import HTMLTestRunner
import unittest
import os

def allCase():
    """定义一个函数，封装discover加载测试用例的方法"""
    case_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)))  # 获取当前工作目录（用例也放在该目录下）
    suite = unittest.TestSuite()  # 定义一个测试套件
    discover = unittest.defaultTestLoader.discover(case_dir,pattern='test*.py',top_level_dir=None) # discover 方法筛选出来的用例，循环添加到测试套件中
    print(discover)
    for test_suite in discover:
       for test_case in test_suite:
           suite.addTests(test_case)
    return suite

if __name__ == '__main__':
    laowang = allCase()
    # runner = unittest.TextTestRunner()
    #now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = 'C:\\Users\\dongs\Desktop\\report.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='自动化测试报告',
                            description='详细测试用例结果 ')
    runner.run(laowang)

