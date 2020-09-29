import joblib
from reg_model import train_pipeline
from reg_model.config import config
from reg_model.preprocessing.data_management import load_dataset,load_pipeline
from reg_model.predict import make_prediction
from sklearn.metrics import r2_score


trc=config.trc

if __name__ == "__main__":
    
   
    print("Test is starting ...")

    test_data=load_dataset(config.DATASET_PATH,"test_data.csv")

    # Split train data
    X_ts=test_data.drop(columns=trc.target_name)
    y_ts=test_data[trc.target_name]
    
    res=make_prediction(X_ts)
    
    #pipe_model=load_pipeline(trained_model_path=config.TRAINED_MODEL_PATH,
    #                        model_name=f"pipe_{trc.model_name}_{trc.model_version}")


    #pred_ts=pipe_model.predict(X_ts)
    print("R2 Score:",r2_score(y_ts,res))
    print("Test is finished ...")