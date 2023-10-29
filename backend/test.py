from flask import Flask,request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, location = 'args',required=True)

class MyResource(Resource):
    def get(self):
        args = parser.parse_args()
        name = args.get('name')
        # 在这里处理 GET 请求逻辑
        return {'message': f'Hello, {name}!'}

api.add_resource(MyResource,'/myresource')
print()
if __name__ == '__main__':
    app.run()