# -*- coding:utf-8 -*-
# @Time      :2020/4/20
from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='Plugins_session_UploadFile',
    ext_modules=cythonize("Plugins_session_UploadFile.py"),
)

# python3 setup.py build_ext --inplace