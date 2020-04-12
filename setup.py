# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in agrierp/__init__.py
from agrierp import __version__ as version

setup(
	name='agrierp',
	version=version,
	description='Change it Later',
	author='Lab51.org',
	author_email='hello@lab51.org',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
