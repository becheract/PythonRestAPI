#import dependencies
from flask import Flask 
from flask_restful import Api, Resource

#create app
app = Flask(__name__)
api = Api(app)

#create 1st ressource

class HelloWorld(Resource):
    def get(self):
        return {"data": "15 minutes to get into the mainframe"}

    def post(self):
        return {"data": "15 minutes to post into the mainframe"}    

#add to the api
#the second param is the api endpoint
api.add_resource(HelloWorld, "/helloworld")


#start server and application
if __name__ == '__main__':
    app.run(debug=True)
