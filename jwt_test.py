from base64 import decode
from flask import Flask,jsonify,request,make_response
from flask.scaffold import F
import jwt
from functools import wraps

user_data={"name":["stijo","joseph","arun","jose"]}
app=Flask(__name__)
app.config['SECRET_KEY']='very secret'
def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token=request.args.get('token',app.config['SECRET_KEY'])
        datas=jwt.decode(token,app.config['SECRET_KEY'])
        
        for i in user_data["name"]:
         if datas['user']==i:
            response_data=jsonify({ "username":datas['user'],"status":"access granted"})
            return response_data
        response_data=jsonify({ "username":datas['user'],"status":"access denied"}) 
        return response_data
    return decorated
@app.route('/unprotected')
def unprotected():
    return "unprotected"
@app.route('/protected')
@token_required
def protected():
    
    return "protected"
@app.route('/login')
def login():
    auth=request.authorization
    token=jwt.encode({'user':auth.username},app.config['SECRET_KEY'])
    if auth and auth.password=='password':
     ##return jsonify({'token':token.decode('UTF-8')})
     return ("http://127.0.0.1:5000/protected?token="+token.decode('UTF-8'))
    else :
        return "not logged in" 

if __name__=='__main__':
    app.run(debug=True)        