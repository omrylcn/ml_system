from flask import Flask,request,jsonify

test_app=Flask("test")

@test_app.route("/",methods=["GET"])
def test():
    if request.method =="GET":

        return "ok"

@test_app.route("/test_json",methods=["GET"])
def test_json():
    if request.method =="GET":

        return jsonify({"test_json":"ok"})

if __name__ == "__main__":
    test_app.run()
