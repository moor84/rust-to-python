FROM rust:latest as rust-build

RUN mkdir build
COPY rust/src ./build/src
COPY rust/Cargo.toml ./build/Cargo.toml

WORKDIR /build

RUN rustup target add x86_64-unknown-linux-gnu
RUN cargo build --release --target x86_64-unknown-linux-gnu

FROM python:3.7-slim

RUN mkdir app

COPY web/main.py /app/main.py
COPY web/requirements.txt /app/requirements.txt
COPY --from=rust-build /build/target/x86_64-unknown-linux-gnu/release/libmylib.so /app/mylib.so

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["gunicorn", "-w 4", "main:app", "-b", "0.0.0.0:8000"]
