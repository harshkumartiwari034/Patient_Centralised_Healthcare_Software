from flask import request
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint
from flask.views import MethodView
from ..Database.Patient.patient_data import PatientDatabase
from ..role_base_authenticator import check_role

blp = Blueprint('patient details update', __name__, description="receptionist update patient details..")


# This route mainly do take back patient data from the database and send it on frontend
@blp.route('/receptionist/fetch/patients/details')
class GetPatientData(MethodView):
    def __init__(self):
        self.patient_db = PatientDatabase()

    @jwt_required(locations=['headers'])
    @check_role('receptionist')
    def get(self):
        patient_id = request.args.get('patient_id')
        patient_data = self.patient_db.find_patient_through_patient_id(patient_id)
        return patient_data


# This route helps receptionist to update patient data what they change...
@blp.route('/receptionist/update/patients/details')
class UpdatePatientData(MethodView):
    def __init__(self):
        self.patient_db = PatientDatabase()

    @jwt_required(locations=['headers'])
    @check_role('receptionist')
    def patch(self):
        patient_id = request.args.get('patient_id')
        updated_data = request.get_data()
        result = self.patient_db.update_patient_data(patient_id, updated_data)
        return result
