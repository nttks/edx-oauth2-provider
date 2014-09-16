#!/usr/bin/env python

from setuptools import setup

setup(
    name='edx-oauth2-provider',
    version='0.1.0',
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
    packages=['oauth2_provider'],
    install_requires=[
        'django-oauth2-provider',
        'PyJWT==0.2.1'
    ],
    dependency_links=[
        'git+https://github.com/edx/edx-oauth2-provider.git@v0.2.7-dev+edx#egg=django-oauth2-provider-0.2.7-dev+edx',
    ]
)
