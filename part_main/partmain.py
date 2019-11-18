import unittest
import requests
from port_method.normaldiff_method import ptsj
from port_method.hot_method import hot_method


def part_use():
    test1 = unittest.TestSuite()
    test1.addTest(ptsj('test1_port200'))
    test1.addTest(hot_method('test4_msg'))
    return test1


if __name__ == '__main__':
    with open('./log.txt','a',encoding='utf8')as f:
        runner = unittest.TextTestRunner(stream=f,verbosity=2)
        runner.run(part_use())


