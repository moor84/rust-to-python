from setuptools import setup
from Cython.Build import cythonize

setup(
    name="mylib_cython",
    version="1.0",
    ext_modules=cythonize("mylib_cython/mylib.pyx"),
    packages=["mylib_cython"],
)
