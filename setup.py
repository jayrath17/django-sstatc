import ez_setup
from setuptools import setup, find_packages


ez_setup.use_setuptools()

setup(
    name = 'django-sstatic',
    version = '0.1',
    packages = find_packages(),
    author = 'Svyatoslav Bulbakha',
    author_email = 'ad3w.inbox@gmail.com',
    description = 'Simple static files versioning for django.',
    url = 'https://bitbucket.org/ad3w/django-sstatic',
    include_package_data = True
)
