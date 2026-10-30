from flask.views import MethodView
from flask_jwt_extended import create_access_token
from flask_smorest import Blueprint, abort
from ..Database.Staff.staff_data import StaffDatabase
from ..Schemas.Receptionist.receptionist_login_schema import StaffLogin, StaffLoginResponseSchema
import hashlib
from datetime import timedelta

blp = Blueprint(
    "staff_login",
    __name__,
    description="receptionist login APIs"
)


@blp.route('/receptionist/login')
class DoctorLogin(MethodView):
    def __init__(self):
        self.staff_db = StaffDatabase()

    @blp.arguments(StaffLogin)
    @blp.response(200, StaffLoginResponseSchema)
    def post(self, data):
        email = data['email']
        password = data['password']
        staff_data, status_code = self.staff_db.staff_exist(email)
        hash_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if staff_data and status_code == 200:
            if staff_data['password'] == hash_password:

                if staff_data['role'] == 'receptionist':
                    access_token = create_access_token(identity=email,
                                                       additional_claims=({'role': staff_data['role']}),
                                                       expires_delta=timedelta(hours=5))
                    return {
                        "message": "Receptionist login successfully.",
                        "access_token": access_token
                    }
                else:
                    abort(403, message='not authorised')
            else:
                abort(401, message='incorrect password')
        else:
            abort(404, message='user not found..')
