from unittest import TestCase
from django_form_asserts import FormTestMixin

from django import forms


class ModlyPotatoForm(forms.Form):
    is_moldy = forms.BooleanField(required=False)
    is_bacterial = forms.BooleanField(required=True)


class PotatoFormTests(FormTestMixin, TestCase):
    form_class = ModlyPotatoForm
    valid_attrs = {"is_moldy": True, "is_bacterial": False}

    def test_is_moldy_field(self):
        self.assertBooleanField("is_moldy", required=False)

    def test_is_bacterial_field(self):
        self.assertBooleanField("is_bacterial", required=True)

    def test_is_bacterial_field_with_default(self):
        self.assertBooleanField("is_bacterial")
