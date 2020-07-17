# Extending Python with Rust

This repository contains code for the article [How to use Rust to extend Python](https://codeburst.io/how-to-use-rust-to-extend-python-360174ee5819).

## Contents

* `rust` - example Rust project - a Python extension
* `package` - example Python PyPI package with an extesion written in Rust
* `web` - example Python web-service (Flask) that uses a Rust extension
* `Dockerfile`, `Dockerfile.pypi` - Docker build scripts for the web service
* `cython` - example Cython project (for comparison)
* `benchmark` - simple benchmark: Rust extension against pure Python and Cython
