import requests
import unittest
from updata_port.port import *

class hot_method(unittest.TestCase):
    def test3_200(self):
        hot = hotapiv3.json()
        self.assertEqual(200,hot['code'])
    def test4_msg(self):
        """测试热升级下发信息"""
        normaldiff = normaldiffapiv3.json()
        if self.assertEqual(201,normaldiff['code']):
            return ( '{}'.format(normaldiff['msg']))
        else:
            return ( '接口请求失败')


if __name__ == '__main__':
    unittest.main()