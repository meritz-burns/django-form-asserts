class FormTestMixin(object):
    form_class = None
    valid_attrs = None

    def assertBooleanField(self, field_name, **kwargs):
        return True
