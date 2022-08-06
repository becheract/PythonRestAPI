#import dependencies
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

#create app
app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="likes of the video is required", required=True)

#object
videos = {}

def abort_video_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Video could not be found")

def abort_video_if_exist(video_id):
    if video_id in videos:
        abort(409, message="Video already exists with that ID")
        
#create 1st ressource
class Video(Resource):
    def get(self, video_id):
        abort_video_doesnt_exist(video_id)
        return videos[video_id]
    
    def put(self, video_id):
        abort_video_doesnt_exist(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201
    
    def delete(self, video_id):
        abort_video_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204

#add to the api
#the second param is the api endpoint
#use angle brackets to pass in params
api.add_resource(Video, "/video/<int:video_id>")


#start server and application
if __name__ == '__main__':
    app.run(debug=True)
