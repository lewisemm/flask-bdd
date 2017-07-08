import json

from flask import request

from app.application import app

USERS = {}


@app.route("/user/<username>", methods=['GET'])
def access_users(username):
    if request.method == 'GET':
        user_details = USERS.get(username)
        if user_details:
            return json.dumps(user_details)
        else:
            return Response(status=404)
