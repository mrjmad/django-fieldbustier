from decimal import Decimal

from django.core.exceptions import FieldError
from django.test import TestCase

from demo_app.models import DummyModel


class DummyModelModifiedWithFieldBustierTest(TestCase):
    def test_dummy_charfield(self):
        dummy_instance = DummyModel.objects.create(char_field="a_long_name_more_than_twelve_characters")
        dummy_instance.refresh_from_db()
        self.assertEqual(dummy_instance.char_field, "a_long_name_more_than_twelve_characters")

    def test_dummy_default_decimalfield(self):
        dummy_instance = DummyModel.objects.create()
        self.assertEqual(dummy_instance.decimal_field, 2.3)

    def test_dummy_value_decimalfield(self):
        dummy_instance = DummyModel.objects.create(decimal_field=Decimal("1.234"))
        dummy_instance.refresh_from_db()
        self.assertEqual(dummy_instance.decimal_field, Decimal("1.234"))

    def test_dummy_integerfield(self):
        with self.assertRaises(FieldError):
            DummyModel.objects.filter(int_field=12)

    def test_new_dummy_charfield(self):
        DummyModel.objects.create(new_char_field="new field!")
        self.assertEqual(DummyModel.objects.all().first().new_char_field, "new field!")
