from setuptools import setup, find_packages

setup(
    name="DjangoFormAsserts",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        'docutils>=0.3',
        "Django >= 1.5.1",
    ],

    author="Mike Burns and Rebecca Meritz",
    author_email="rebecca@meritz.com",
    description='This provides a DjangoFormTestCase that adds assertions that make it easier to test form validations.',
    license="BSD",
    keywords="django form testing assertions",
    url='https://github.com/meritz-burns/django-form-asserts',

    tests_require=["nose", "mock"],
    test_suite="nose.collector",
)
