import sys

from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="mylib-rust",
    version="1.0",
    rust_extensions=[RustExtension("mylib.mylib", binding=Binding.RustCPython)],
    packages=["mylib"],
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
    long_description="This is a description for our Rust-Python package.",
    long_description_content_type="text/x-rst"
)
