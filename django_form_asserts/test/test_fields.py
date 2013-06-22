from django import forms
import unittest
from unittest import TestCase


class TestFields(TestCase):
    def build_form(self, field_name, field):
        form = forms.Form()
        form.fields[field_name]=field
        return form

    def runAssertion(self, assertion, form, field_name, **kwargs):

    
    def test_boolean_field(self):
        field = forms.BooleanField()
        form = self.build_form("is_cute", field)
        self.runAssertion(self.assertBooleanField, form, 'is_cute')

    def test_boolean_field_required(self):
        field = forms.BooleanField(required=True)
        form = self.build_form("is_cute", field)
        self.runAssertion(self.assertBooleanField, form, 'is_cute', required=True)

if __name__ == '__main__':
    unittest.main()
