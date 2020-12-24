import unittest
from datetime import datetime

import requests
from BeautifulReport import BeautifulReport as br

from config import config_util as cu


class TestUser(unittest.TestCase):
    base_url = None

    @classmethod
    def setUpClass(cls):
        cls.base_url = cu.get_options('base', 'url')

    def test_user_register(self):
        """
        测试用户注册
        :return:
        """
        # r = requests.post(base_url + '/users/register',
        #                   json=json.loads(cu.get_options('user_register', 'data')))
        r = requests.post(self.base_url + '/users/register', headers={'Content-Type': 'application/json;charset=UTF-8'},
                          data=cu.get_options('user_register', 'data').encode('utf-8'))
        result = r.json()
        self.assertEqual(result['code'], 0, result['msg'])


# suite = unittest.TestSuite()  # 定义一个测试集合
# suite.addTest(unittest.makeSuite(TestUser))  # 把写的用例加进来（将TestUser类）加进来
# run = br(suite)  # 实例化BeautifulReport模块
# run.report(filename='test_report-%s' % datetime.now().strftime('%Y-%m-%d %H:%M:%S'), description='用户测试')
