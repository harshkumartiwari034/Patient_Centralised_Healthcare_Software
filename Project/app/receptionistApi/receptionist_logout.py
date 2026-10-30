from flask import jsonify

from .Blocklist import Blocklist
from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt, unset_jwt_cookies

blp = Blueprint('receptionist logout', __name__, description='calling this api receptionist logout.....')


@blp.route('/receptionist/logout')
class PatientLogout(MethodView):
    @jwt_required(locations=['headers'])
    def post(self):
        jti = get_jwt()['jti']
        Blocklist.add(jti)
        response = jsonify({"message": 'receptionist logout successfully...'})
        unset_jwt_cookies(response)
        return response, 200
