from distutils.core import setup
import io
import os
import sys
from shutil import rmtree
from setuptools import find_packages, setup, Command

setup(
  name = 'TechLearn',         # How you named your package folder
  packages = ['kits'],   # Chose the same as "name"
  version = '1.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'TestProgram',   # Give a short description about your library
  author = 'WhereIsTom',                   # Type in your name
  author_email = 'wzzhangzheyuan@163.com',      # Type in your E-Mail
  url = 'https://github.com/GodOn514/TechLearn',   # Provide either the link to your github or to your website
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best

)
