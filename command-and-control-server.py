from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

win_cmds = {'cmd_id': "dir"}
osx_cmds = {'cmd_id': "ls"}


class WinCmdControl(Resource):
    def get(self):
        return win_cmds['cmd_id']

    def put(self):
        win_cmds['cmd_id'] = request.data
        print request.data
        return {'cmd_id': win_cmds['cmd_id']}


class OsxCmdControl(Resource):
    def get(self):
        return osx_cmds['cmd_id']

    def put(self):
        osx_cmds['cmd_id'] = request.data
        print request.data
        return {'cmd_id': osx_cmds['cmd_id']}

api.add_resource(WinCmdControl, '/win')
api.add_resource(OsxCmdControl, '/osx')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
