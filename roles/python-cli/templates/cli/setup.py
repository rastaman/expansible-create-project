# -*- coding: utf-8 -*-
"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from {{ template_name }} import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as readme_file:
    long_description = readme_file.read()


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov={{ template_name }}', '--cov-report=term-missing'])
        raise SystemExit(errno)


setup(
    name='{{ template_name }}',
    version=__version__,
    description='A command line client for {{ template_name | capitalize }}.',
    long_description=long_description,
    url='{{ scm_url }}',
    author='{{ author }}',
    author_email='{{ author_email }}',
    license='WTFPL',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='cli',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=['docopt'],
    extras_require={
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points={
        'console_scripts': [
            '{{ template_name }}={{ template_name }}.cli:main',
        ],
    },
    cmdclass={'test': RunTests},
)
