# A. Firt Stage : `MLOps level 1: Manual process`

This part provides a basic primative ML-project. It is similar reference article. It is a regression model. It uses famous house-price data. The model schema looks like below image.

![firt_part](docs/image/ml-level-1.png)
=======

## Summary of the model

- There are three main parts like `data processing,training and prediction`.
- `pipeline` : scikit-learn - model is saved as pipeline
- `Docker` : model prediction service is a docker image  
- `.yml`:format of model config files


## Notes

- There is a python package(wheel file) that is called reg_model in `local_area/package_files/dist` path. It can be installed via `pip`.
- To run `docker files`  checks `notes.md` in docker folder.

## To Do List

- [x] Model Training
- [x] Model Saving and Making Package
- [x] Model Serving

