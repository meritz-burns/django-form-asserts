from django import forms
import unittest
from unittest import TestCase

from django_form_asserts import FormTestCase


class TestFields(TestCase):
    def build_form(self, field_name, field):
        form = forms.Form()
        form.fields[field_name] = field
        return form

    def build_form_class(self, form):
        klass = type("tmp_form_class", (forms.Form,), {})
        klass.fields = form.fields
        return klass

    def build_test_case(self, form, valid_attrs):
        form_class = self.build_form_class(form)
        test_case = FormTestCase('runTest')
        test_case.form_class = form_class
        test_case.valid_attrs = valid_attrs
        return test_case

    def test_boolean_field(self):
        field = forms.BooleanField()
        valid_attrs = {"is_cute": True}
        form = self.build_form("is_cute", field)
        form.is_cute = True
        test_case = self.build_test_case(form, valid_attrs)
        test_case.assertBooleanField('is_cute')
        form.is_cute = False
        test_case = self.build_test_case(form, valid_attrs)
        test_case.assertBooleanField('is_cute')
        form.is_cute = None
        test_case = self.build_test_case(form, valid_attrs)
        test_case.assertBooleanField('is_cute')

    #def test_boolean_field_required(self):
    #    field = forms.BooleanField(required=True)
    #    form = self.build_form("is_cute", field)
    #    self.runAssertion(self.assertBooleanField, form, 'is_cute', required=True)

if __name__ == '__main__':
    unittest.main()
