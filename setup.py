#!/usr/bin/env python

from sys import platform
import subprocess
from setuptools import setup


setup(name='test',
      version='0.1',
      description='Bla',
      author='Shane Fagan',
      author_email='mail@example.com',
      url='http://example.com',
      license='MIT',
      packages=['bin'],
      install_requires=[],
      scripts=['bin/main']
      ),

