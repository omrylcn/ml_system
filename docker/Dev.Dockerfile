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
  
WORKDIR /app 

#COPY reg_model reg_model
#COPY requirements.txt .
#COPY trial.py .

#RUN pip3 install -r requirements.txt

#CMD ["python3","trial.py"]