docker build -f Dockerfile.pypi -t rust-python-web-pypi .
docker run -p 8000:8000 rust-python-web-pypi
