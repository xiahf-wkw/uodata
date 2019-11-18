import requests
import unittest
from updata_port.port import *

class ptsj(unittest.TestCase):
    def test1_port200(self):
        """测试接口是否200"""
        normaldiff = normaldiffapiv3.json()
        self.assertEqual(201,normaldiff['code'])
    def test2_msg(self):
        """测试是否需要升级"""
        normaldiff = normaldiffapiv3.json()
        if self.assertEqual(201,normaldiff['code']):
            return ( '{}'.format(normaldiff['msg']))
        else:
            return ( '接口请求失败')
if __name__ == '__main__':
    unittest.main()

