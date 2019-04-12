import unittest


class TestMethod(unittest.TestCase):
    def setUp(self):
        self.number = None

    def test_case_01(self):
        print('This is test 01')
        globals()['number'] = '50001'

    @unittest.skip('test_case_02')
    def test_case_02(self):
        print('This is test 02')

        #print('The number is:{0}'.format(self.number))


if __name__ == '__main__':
    unittest.main()



