from datetime import date
from unittest.mock import patch

from django.test import TestCase
from .greet import sayHello, function_to_get_today


# Create your tests here.


class DummyTestCase(TestCase):
    def setUp(self):
        return super().setUp()

    def test_dummy_test(self):
        print('dummy_test!')
        self.assertEquals("hello", sayHello())


def fake_today():
    return date(year=2023, month=1, day=28)

class SampleTest(TestCase):
    @patch("api.greet.get_today", fake_today()) # greet.py의 get_today의 함수는 fake_today 함수로 치환
    def test_function_to_get_today_using_mock(self):
        self.assertEqual(function_to_get_today().strftime("%Y-%m-%d"), "2023-01-28")

