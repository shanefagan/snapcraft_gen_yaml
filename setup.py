#!/usr/bin/env python

from sys import platform
import subprocess
from setuptools import setup


setup(name='test',
      version='0.1',
      description='Python Distribution Utilities',
      author='Shane Fagan',
      author_email='shane.fagan@infosys.com',
      url='http://infosys.com',
      license='MIT',
      packages=['bin'],
      install_requires=[],
      scripts=['bin/main']
      ),

