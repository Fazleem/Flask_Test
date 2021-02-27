from flask import Flask, jsonify, request, abort
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)  # wrapper tells us that we are using Rest API (wrapping app as an API)

# @app.route('/<string:name>')
# def hello_world(name:str):
#     # name = request.args.get("name")
#     return jsonify(data=name), 200

"""
create resource using api
this helps us to override the methods inside a Resource like get a request, post a request
--> whenever you are running make sure the return type is serializable
"""

# names = {"fazleem1":{"age":25, "gender":"male"},
#          "fazleem2":{"age":10, "gender":"male"}}
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Required Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Required Views for the video", required=True)
video_put_args.add_argument("likes", type=int, help="Required Likes for the video", required=True)
videos = {}
"""
basic class for reference
class HelloWorld(Resource):
    def get(self, name):
        return names[name]
"""


def abort_video(video_id):
    if video_id not in videos:
        abort(404, "video not available")

def abort_video_exists(video_id):
    if video_id in videos:
        abort(404, "video already exists with the ID")


class Video(Resource):
    def get(self, video_id):
        abort_video(video_id)
        return videos[video_id]

    # create video inside put
    def put(self, video_id):
        abort_video_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        # print(request.form['likes'])
        return videos[video_id], 201

    def delete(self, video_id):
        abort_video(video_id)
        del videos[video_id]
        return 'deleted video', 204



"""register it as a resource
->since it is an api add it to the resource and make it accessable through URL using /helloworld"""
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug=True)
