# Dockerfiles guide

## Dev.Dockerfile
- Training and development dockerfile.
- Commands to run
  - `docker build . -t test-reg -f Dev.Dockerfile`
  - `docker run -it --rm --name test test-reg`
  - If enter  contanier run this : `docker run -it --rm --name test test-reg /bin/bash`
