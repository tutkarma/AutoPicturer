from flask import Flask
from libkeywords import extract, search_tags
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)

EXECUTE = {
    'empty': {'text': 'empty'},
}

def abort_if_todo_doesnt_exist(execute_id):
    if execute_id not in EXECUTE:
        abort(404, message="Todo {} doesn't exist".format(execute_id))

parser = reqparse.RequestParser()
parser.add_argument('text')

class Execute(Resource):
    def get(self):
        return EXECUTE

    def post(self):
        args = parser.parse_args()
        EXECUTE['task'] = {'text': args['text']}

        tags = extract(args['text'])
        url = search_tags(tags)

        return {'url' : url,
                'tags': tags
               }, 201


api.add_resource(Execute, '/execute')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
