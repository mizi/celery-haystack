#!/usr/bin/env python
from os import path
from setuptools import setup, find_packages
from celery_haystack import __version__


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='celery-haystack',
    version=__version__,
    author='Jannis Leidel',
    author_email='jannis@leidel.info',
    url='https://github.com/django-haystack/celery-haystack/',
    description='An app for integrating Celery with Haystack.',
    long_description=long_description,
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
    ],

    install_requires=['django-appconf>=0.4.1'],
    tests_require=[
        'django-discover-runner',
        'django-haystack',
        'celery',
        'Whoosh',
        'flake8',
        'coverage',
    ],

    packages=find_packages(exclude=['tests']),
)
