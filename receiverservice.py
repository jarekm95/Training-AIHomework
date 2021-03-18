import requests
from flask import Flask, request
from flask_restplus import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
todos = {}

@api.route('/api/v1/ping')
class Receiver(Resource):
    def post(self):
        body = request.json
        url = body.get("url")
        url_content = requests.get(url, verify=False).text
        return url_content

@api.route('/api/v1/info')
class Health(Resource):
    def get(self):
        return '{"Receiver": "Cisco is the best!"}'


if __name__ == '__main__':
    app.run(debug=True)