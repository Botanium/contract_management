# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in contract_management/__init__.py
from contract_management import __version__ as version

setup(
	name='contract_management',
	version=version,
	description='Managing Contracts for Businesses (App By Fwrat.com)',
	author='Fwrat.com',
	author_email='admin@fwrat.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
