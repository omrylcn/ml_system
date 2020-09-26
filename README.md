# ML System Project

An example project is ML system project. The first stage will be experimental studies. It is mostly reference and inspiration from [this article](https://cloud.google.com/solutions/machine-learning/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning).
It aims to show how it be MLOps & CI/CD practices with a ML project.

## A. Firt Stage : `MLOps level 0: Manual process`

It is a simple regression model. It uses famous house price data.The model architecture schema looks like below image.
![firt_part](https://cloud.google.com/solutions/images/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning-2-manual-ml.svg)

*Summary of the model* :
  
  - There are three main parts like `data processing,training and prediction`.
  - `pipeline` : scikit-learn - model is saved as pipeline
  - `Docker` : model prediction service is a docker images
  - `.yml` format : model config files   
  
 
## B. Second Stage : `MLOps level 1: Pipeline`

**To DO**
