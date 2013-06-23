===================
Django Form Asserts
===================

This provides a DjangoFormTestCase that adds assertions that make it easier to
test form validations.

------------
Installation
------------

The easiest way is to install using pip::

    pip install django-form-asserts

-----
Usage
-----

Here is an example showing the custom assertions::

    from django_form_asserts import FormTestCase

    class PotatoFormTests(FormTestCase):
        form_class = PotatoForm
        valid_attrs = {"type": "red-bliss",
                       "quantity": 5,
                       "number_of_eyes": 44,
                       "is_moldy": True,
                       "country_of_origin": "Sweden",
                       "birthday": Datetime(}

        def test_valid_form(self):
            self.assertValid()

        def test_is_moldy_field(self):
            self.assertBooleanField("is_moldy", required=False)

        def test_type_field(self):
            self.assertCharField("type", min_length=1)

        def test_country_of_origin_field(self):
            self.assertChoiceField("country_of_origin",
                                   choices=PotatoForm.COUNTRY_CHOICES)

------------
Contributing
------------

* Practice test-driven design.
* The test suite can be run using `setuptools`.
* We love feature branches.

Quick start::

    $ mkvirtualenv django-form-asserts
    $ python setup.py test

-------
License
-------

Copyright 2013 Rebecca Meritz and Mike Burns. Distributed under the BSD license.
