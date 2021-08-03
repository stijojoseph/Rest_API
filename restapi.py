from flask import Flask,jsonify,request


js={
"name":"joseph",
"age":30,
"cars":["Ford", "BMW", "Fiat"]
}

app=Flask(__name__)

@app.route('/')
def home():
    return jsonify(js)

@app.route('/store',methods=['POST'])
def home1():
    return jsonify(js['id'])

@app.route('/store/json/data',methods=['POST'])
def home3():
    json_data=request.get_json(force=True)
    if json_data['name']==js['name']:
     return jsonify(js['cars'])
    else:
      return "data not found"  

@app.route('/store/<string:name>',methods=['POST'])
def home2(name):
    if js['name']==name:
        return jsonify(js)
    else:
        return "name not authenticated"    

app.run()