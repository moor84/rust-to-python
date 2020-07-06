docker build -f Dockerfile -t rust-python-web .
docker run -p 8000:8000 rust-python-web
