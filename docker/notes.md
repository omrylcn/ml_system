# Dockerfiles guide

## Usage 
- must move docker files to main path  for running


## Dev.Dockerfile
- Training and development dockerfile.
- Commands to run
  - `docker build . -t test-reg -f Dev.Dockerfile`
  - `docker run -it --rm --name test test-reg`
  - If enter  contanier run this : `docker run -it --rm --name test test-reg /bin/bash`

## Pred.Dockerfile (Api File)
- Serving File to predict data.
- Commands to run
  - `docker build . -t test-pred -f Pred.Dockerfile`
  - `docker run -it --rm --name test  -p 5000:5000 test-pred`
  - If enter  contanier run this : `docker run -it --rm --name test -p 5000:5000  test-pred /bin/bash`
