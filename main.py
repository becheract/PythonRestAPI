#import dependencies
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
#create app
app = Flask(__name__)
api = Api(app)
#db config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
#define the models

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #nullable = false : has to have information
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {name}, views = {views}, likes = {likes})"

#creates the database
db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="likes of the video is required", required=True)
      

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="name of the video is required")
video_update_args.add_argument("views", type=int, help="views of the video is required")
video_update_args.add_argument("likes", type=int, help="likes of the video is required")
      
#how it will be serialized
resource_fields = {
    'id': fields.Integer,
    'name' : fields.String,
    'views': fields.Integer,
    'likes' : fields.Integer,
}
#create 1st ressource
class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(409, message="Could not find Video with thtat ID!")
        return result
    
    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video id taken")
        video = VideoModel(
            id=video_id,
            name=args['name'],
            views=args['views'],
            likes=args['likes'])
            
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video doesn't exist, cannot update.")

        if args['name']:
            result.name = args["name"]
        if args['views']:
            result.views = args["views"]
        if args['likes']:
            result.likes = args["likes"]

        db.session.commit()

        return result
    
    @marshal_with(resource_fields)
    def delete(self, video_id):
        result = VideoModel.query.filter(id=video_id).delete()
        db.session.commit()
        return '', 204

#add to the api
#the second param is the api endpoint
#use angle brackets to pass in params
api.add_resource(Video, "/video/<int:video_id>")


#start server and application
if __name__ == '__main__':
    app.run(debug=True)
