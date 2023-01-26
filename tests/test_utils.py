from unittest import TestCase
from crawler.utils import Utils


class TestUtils(TestCase):
    def test_write_file(self):
        # GIVEN 
        my_list = ['a', 'b', 'c', 'd']
        path = './file.txt'
        utils = Utils()
        # WHEN
        utils.write_txt_file(path=path, document=my_list)
        # THEN
        self.assertIsInstance(utils, Utils)