FROM python:3.6-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends\ 
    gcc \
    g++ \
    git \
    build-essential\
    cmake
        
RUN git clone --recursive --branch stable --depth 1 https://github.com/Microsoft/LightGBM

RUN cd LightGBM/python-package && python setup.py install && apt-get autoremove -y
  
WORKDIR  /app 


COPY model_serving model_serving

# not use !
#ENV PIP_EXTRA_PATH=/app/model_serving/package


# install server packages
RUN pip3 install -r model_serving/requirements.txt

# install model packages
RUN pip3 install model_serving/package/$(ls model_serving/package|grep .whl)

  
WORKDIR  /app/model_serving/


CMD ["python3","test.py"]