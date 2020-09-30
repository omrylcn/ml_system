# ML System Project

It is a ML system project.This repo aims to show how it be MLOps & CI/CD practices with a ML project. There are three stages. Each stages are more complex and complete than previous stage.

- First stage is simple-basic studies. It is mostly reference and inspiration from [this article](https://cloud.google.com/solutions/machine-learning/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning).

- Second stage is more complex than first stage. It contains extra parts like data pipeline and testing.

- Third stage is final stage. It contains modern ML-system project that is gained some modern skill and abilities like MLOps, CI&CD and data pipelines.

## A. Firt Stage : `MLOps level 0: Manual process`

This part provides a basic primative ML-project. It is similar reference article. It is a regression model. It uses famous house price data. The model architecture schema looks like below image.

![firt_part](https://cloud.google.com/solutions/images/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning-2-manual-ml.svg)

### Notes

- There is a python package(whl file) that is called reg_model.It can be installed via 'pip'.
- To run docker files, check "notes.md" in docker folder.

### Summary of the model

- There are three main parts like `data processing,training and prediction`.
- `pipeline` : scikit-learn - model is saved as pipeline
- `Docker` : model prediction service is a docker image  
- `.yml`:format of model config files

## B. Second Stage : `MLOps level 2: Pipeline`

## C. Third Stage : `MLOps level 3: CI&CD`

## References

- <https://cloud.google.com/solutions/machine-learning/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning>

- <https://www.trainindata.com/feature-engine>

- <https://github.com/solegalli/deploying-machine-learning-models>


**To Do**
