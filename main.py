import unittest
from datetime import datetime

from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    suite_tests = unittest.defaultTestLoader.discover("./test_case", pattern="*", top_level_dir=None)
    BeautifulReport(suite_tests).report(filename='测试报告-%s' % datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                        description='', report_dir='./test_report')
