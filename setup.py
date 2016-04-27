#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>

from setuptools import setup, find_packages
from cosmos import __version__

tests_require = [
    # 'mock',
    'factory_boy',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    # 'tox',
    'ipdb',
    # 'coveralls',
    # 'sphinx',
]

setup(
    name='cosmos',
    version=__version__,
    description='cosmos is an open-source platform-agnostic database as a service solution.',
    long_description='''
cosmos is an open-source platform-agnostic database as a service solution.
''',
    keywords='dbaas cloud amazon',
    author='Bernardo Heynemann',
    author_email='heynemann@gmail.com',
    url='https://github.com/heynemann/cosmos',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'tornado',
        'redis',
        'redisco==0.1.0',
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'cosmos=cosmos.cli:main',
        ],
    },
)
