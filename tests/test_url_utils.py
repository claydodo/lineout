from unittest import TestCase
from src.lineout.url import *


class TestUrlUtils(TestCase):
    def test_get_detail_url(self):
        self.assertEqual(get_detail_url('/api/some/', 3), '/api/some/3/')
        self.assertEqual(get_detail_url('/api/some/', 'a'), '/api/some/a/')

    def test_url_add_params(self):
        self.assertEqual(url_add_params('/api/some/', {'a': 3, 'b': 'test'}), '/api/some/?a=3&b=test')
        self.assertEqual(url_add_params('http://some.com/api/some/', {'a': 3}), 'http://some.com/api/some/?a=3')
        self.assertEqual(url_add_params('/api/some/?b=test', {'a': 3}), '/api/some/?b=test&a=3')
