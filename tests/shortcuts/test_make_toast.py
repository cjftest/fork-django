from django.shortcuts import make_toast
from django.test import SimpleTestCase
from django.utils import timezone
from django.http import HttpResponse


class MakeToastTests(SimpleTestCase):
    def test_make_toast(self):
        self.assertEqual(make_toast(), "toast")
