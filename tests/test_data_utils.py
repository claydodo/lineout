from unittest import TestCase
from src.lineout.data import *


class TestDataUtils(TestCase):
    def test_get_result_list(self):
        sample_list = [{'id': 1, 'name': 'a'}, {'id': 2, 'name': 'b'}]
        paginated = {
            'count': 2,
            'previous': None,
            'next': None,
            'results': sample_list
        }
        not_paginated_1 = {
            'foo': 'bar'
        }
        not_paginated_2 = {
            'results': {'foo': 'bar'}
        }

        self.assertListEqual(get_result_list(sample_list), sample_list)
        self.assertListEqual(get_result_list(paginated), sample_list)

        with self.assertRaises(ValueError):
            get_result_list(not_paginated_1)

        with self.assertRaises(ValueError):
            get_result_list(not_paginated_2)
