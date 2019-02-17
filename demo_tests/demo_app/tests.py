from decimal import Decimal

from django.db.utils import DataError
from django.test import TestCase

from .models import DummyModel


class DummyModelUnModifiedTest(TestCase):
    def test_dummy_charfield(self):
        with self.assertRaises(DataError):
            DummyModel.objects.create(char_field="a_long_name_more_than_twelve_characters")

    def test_dummy_integerfield(self):
        dummy_instance = DummyModel.objects.create(int_field=12)
        self.assertEqual(dummy_instance.int_field, 12)

    def test_dummy_default_decimalfield(self):
        dummy_instance = DummyModel.objects.create()
        self.assertEqual(dummy_instance.decimal_field, 0)

    def test_dummy_value_decimalfield(self):
        dummy_instance = DummyModel.objects.create(decimal_field=Decimal("1.234"))
        dummy_instance.refresh_from_db()
        self.assertNotEqual(dummy_instance.decimal_field, Decimal("1.234"))
        self.assertEqual(dummy_instance.decimal_field, Decimal("1.23"))
