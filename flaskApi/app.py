import os

from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
import werkzeug
import pandas as pd
import json

app = Flask(__name__)
CORS(app)
api = Api(app)


dir_path = os.path.dirname(os.path.realpath(__file__))
RATING_FOLDER = "ratings/"




class GetRatingsAPI(Resource):
   def get(self):
     parse = reqparse.RequestParser()
     parse.add_argument('user')
     args = parse.parse_args()
     path = RATING_FOLDER + args.user +'.json'
     with open(path) as json_data:
        data = json.load(json_data)
     return data




         
class HelloWorld(Resource):    
     def get(self):        
         return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(GetRatingsAPI,'/getRatings')




if __name__ == "__main__":
    app.debug = True
    app.run(debug=True)
    app.debug = True

# run app using flask run --host=0.0.0.0