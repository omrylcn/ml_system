from flask import Flask,request,jsonify
from pydantic import  BaseModel
import pickle


app=Flask(__name__)

class QueryModel(BaseModel):
    name:str


@app.route("/test",methods=["GET"])
def test():
    if request.method == "POST":
        image = pickle.loads(request.get_data())
        print(image.shape)
    return "ok"

