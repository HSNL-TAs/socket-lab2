from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

cmds = {'cmd_id': "ls"}


class CmdControl(Resource):
    def get(self):
        return cmds['cmd_id']

    def put(self):
        cmds['cmd_id'] = request.data
        return {'cmd_id': cmds['cmd_id']}

api.add_resource(CmdControl, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
