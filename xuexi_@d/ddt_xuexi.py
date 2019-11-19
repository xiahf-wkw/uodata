import requests
import unittest
from ddt import ddt,data,file_data
from updata_port.port import *


@ddt
class ptsh(unittest.TestCase):

    @file_data('./pt_updata.json')
    def test_xm(self,authkey,data):
        value = {"authkey" :authkey,
                 "xuexi_@d":data}
        print(type(value))
        r = requests.post(url='http://update.app.2345.com/backend/index.php?r=NormalDiffApiV3&&test&test',data = value)
        c = r.text
        print(c)


if __name__ == '__main__':
    unittest.main(verbosity=2)

