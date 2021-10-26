# -*- coding:utf-8 -*-
# @Time      :2020/4/20
from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='Plugins_test',
    ext_modules=cythonize("Plugins_test.py"),
)

# python3 setup.py build_ext --inplace