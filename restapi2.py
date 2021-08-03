from flask import Flask, request,jsonify
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT,jwt_required
from security import authenticate,identity
import jwt
from functools import wraps

user_data={"name":["stijo","joseph","arun","jose","bobby"]}
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
data=[]

api = Api(app)

class student(Resource):
    @token_required
    def get(self,name):
        return jsonify(data)
    def post(self,name):
        item={"name": name}
        data.append(name)
        return "update success"
class tokens(Resource):
    def get(self,name):
     auth=request.authorization
     token=jwt.encode({'user':auth.username},app.config['SECRET_KEY'])
     if auth and auth.password=='password':
     ##return jsonify({'token':token.decode('UTF-8')})
      return ("http://127.0.0.1:5000/protected?token="+token.decode('UTF-8'))
     else :
        return "not logged in" 
    def post(self,name):
        #item={"name": name}
        user_data["name"].append(name)
        return "update success"

api.add_resource(student,'/protected')
api.add_resource(tokens,'/login/<string:name>')
app.run(port=5000)        