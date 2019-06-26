#-*- coding:utf-8 -*
import unittest  # 导入unittest
import requests  # 导入requests库
import json  # 导入json
import HTMLTestRunner

'''
TestCase 也就是测试用例

TestSuite 多个测试用例集合在一起，就是TestSuite

TestLoader是用来加载TestCase到TestSuite中的

TestRunner是来执行测试用例的,测试的结果会保存到TestResult实例中，包括运行了多少测试用例，成功了多少，失败了多少等信息
'''

class ceshi(unittest.TestCase):  # 定义一个类，类的首字母要大写哦
    def setUp(self):
        print("测试用例执行前的初始化操作========")
    def tearDown(self):
        print("测试用例执行完之后的收尾操作=====")
    def test_get1(self):  # 定义一个方法，切记要以test开头哦   #params
        u'''get请求接口'''
        self.url ='http://tdr-authstru.intra.sit.beyonds.gw/v1/user/list'
        headers = {'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyTmFtZSI6ImFkbWluIiwidXNlcklkIjoxfQ.QzQam28P2eFUmtTaj_sHTiWYVuCWXjKLErLO8YkBah0'}
        r = requests.get(self.url, headers=headers)  # 传入参数
        result = r.json()
        # result = json.loads(r.text)  # 使用json格式返回
        self.assertEqual(result['status'], 200,'测试成功')  # 检验返回值，断言是否相等
        self.assertEqual(result['code'], '000000','测试成功')   #断言检查code
        print('url:', self.url, '\n', 'request_headers:', headers, '\n', 'response:', result)

    def test_post1(self):
        u'''post请求接口'''
        self.url = 'http://tdr-authstru.intra.sit.beyonds.gw/v1/user/addRole'
        userid = [1783]
        for user_id in range(len(userid)):
            data = {'userId': userid[user_id], 'roleId': 142033}
            headers = {"Content-Type":"application/Json",'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyTmFtZSI6ImFkbWluIiwidXNlcklkIjoxfQ.QzQam28P2eFUmtTaj_sHTiWYVuCWXjKLErLO8YkBah0'}
            r = requests.post(self.url,json=data, headers=headers)  # 传入参数
            result =r.json()  #使用json格式返回
            # result = json.loads(r.text)  # 使用json格式返回
            self.assertEqual(result['message'],'成功','测试成功')  # 检验返回值，断言是否相等 断言添加注释'测试成功'
            self.assertEqual(result['code'],'000000','测试成功')  # 断言检查code
            print ('url:',self.url,'\n','request:',data, '\n', 'response:', result)
            print (' ')
if __name__ == "__main__":
    unittest.main()

# if __name__ == '__main__':
#     """
#     unittest执行过程：
#                     1.新建测试类且继承于：unittest.TestCase
#                     2.重写setUp()初始化函数和tearDown()清理/拆解函数
#                     3.以test开头定义测试函数
#                     4.用装饰器@unittest.skip()跳过测试用例
#                     5.在程序入口if __name__ == '__main__'：中实例化测试套件： suite = unittest.TestSuite()
#                     6.实例化测试套件加载器：loader = unittest.TestLoader()
#                     7.测试套件对象suite调用addTests()方法,将测试用例加载器对象loader调用loadTestFromTestCase(测试类名)获取的用例添加到测试用例中
#                     8.调用HTMLReport.TestRunner()方法实例化测试用例执行器runner
#                     9.测试用例执行器runner调用run()方法执行测试套件suite并生成报告
#     """
#
#     # 测试套件
#     suite = unittest.TestSuite()
#     # 测试用例加载器
#     loader = unittest.TestLoader()
#     # 把测试用例加载到测试套件中
#     suite.addTests(loader.loadTestsFromTestCase(ceshi))
#
#     # 测试报告路径
#     report_path = r"C:\Users\dongs\Desktop\report1.html"
#     report =open(report_path,'wb')
#     runner = HTMLTestRunner.HTMLTestRunner(
#             stream=report,  #stream:测试报告写入文件的存储区域
#             title=u'自动化测试报告', #title:测试报告的主题
#             description=u'详细测试用例结果',    #测试报告的描述,不传默认为空
#         )
#     # 执行测试用例套件
#     runner.run(suite)
#     report.close()

