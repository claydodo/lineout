from unittest import expectedFailure
from django.test import TestCase
from src.lineout.test import APITestMixin


sample_list = [{'id': 1, 'name': 'a'}, {'id': 2, 'name': 'b'}]
paginated = {
    'count': 2,
    'previous': None,
    'next': None,
    'results': sample_list
}


class TestAPITestMixin(APITestMixin, TestCase):
    # TODO: setup some django model/api and test the rest methods

    def test_assertIsListResult(self):
        self.assertEqual(self.assertIsListResult(sample_list), sample_list)
        self.assertEqual(self.assertIsListResult(paginated), sample_list)

    def test_assertIsPaginatedListResult(self):
        self.assertIsPaginatedListResult(paginated)

    @expectedFailure
    def test_not_paginated(self):
        self.assertIsPaginatedListResult(sample_list)
