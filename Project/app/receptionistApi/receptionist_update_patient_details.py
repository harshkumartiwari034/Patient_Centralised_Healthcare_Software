from flask import request
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequest
from flask_smorest import Blueprint
from flask.views import MethodView
from ..Database.Patient.patient_data import PatientDatabase
from .receptionist_patient_search import DoctorFetchPatientInformation
from ..role_base_authenticator import check_role

blp = Blueprint('patient details update', __name__, description="receptionist update patient details..")


@blp.route('/receptionist/update/patients/details')
class UpdatePatientData(MethodView):
    def __init__(self):
        self.patient_db = PatientDatabase()

    @jwt_required(locations=['headers'])
    @check_role('receptionist')
    def patch(self):
        patient_id = request.args.get('patient_id')
