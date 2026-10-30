from .receptionist_login import blp as receptionistLoginBlueprint
from .receptionist_patients_register import blp as receptionistPatientRegisterBlueprint
from .receptionist_patient_search import blp as receptionistPatientSearchBlueprint
from .receptionist_logout import blp as receptionistLogoutBlueprint

def register_receptionist_blueprint(app_api):
    app_api.register_blueprint(receptionistLoginBlueprint)
    app_api.register_blueprint(receptionist_patients_register)
    app_api.register_blueprint(receptionistPatientSearchBlueprint)
    app_api.register_blueprint(receptionistLogoutBlueprint)
