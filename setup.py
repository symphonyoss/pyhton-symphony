#!/usr/bin/env python

'''
    Execution:
        python setup.py build
        python setup.py install
    Purpose:
        This is the setup script for the app
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@nycresistor.com'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

from setuptools import setup, find_packages
from pip.req import parse_requirements


# parse_requirements() returns generator of
# pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt')

# reqs is a list of requirement
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='python-symphony',
    version='0.0.19',
    description='python module for symphony chat',
    author='Matt Joyce',
    author_email='matt@nycresistor.com',
    url='https://github.com/symphonyoss/python-symphony',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='symphony chat api python module',
    # install dependencies from requirements.txt
    install_requires=reqs,
    packages=find_packages(),
    # bin files / python standalone executable scripts
    include_package_data=True,
    zip_safe=False,
)
