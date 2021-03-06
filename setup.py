#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='edx-oauth2-provider',
    version='0.5.8',
    description='Provide OAuth2 access to edX installations',
    author='edX',
    url='https://github.com/edx/edx-oauth2-provider',
    license='AGPL',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    packages=find_packages(exclude=['tests']),
    dependency_links=[
        'git+https://github.com/edx/django-oauth2-provider@0.2.7-fork-edx-6#egg=django-oauth2-provider-0.2.7-fork-edx-6',
    ],
    install_requires=[
        'django-oauth2-provider==0.2.7-fork-edx-6',
        'PyJWT==1.0.1'
    ]
)
