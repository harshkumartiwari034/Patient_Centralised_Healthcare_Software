from flask_smorest import Blueprint
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt
from ..Database.Patient.Otp_data import PatientOtpDatabase
import secrets
from flask_mail import Message
from ..extensions import mail
from flask import current_app

blp = Blueprint("Make secure patient access medical records", __name__)


@blp.route("/generate/otp/")
class MakeSecurePatientAccessMedicalRecords(MethodView):
    def __init__(self):
        self.otp = PatientOtpDatabase()

    @jwt_required(locations=['headers'])
    def post(self):
        patient_credentials = get_jwt()
        patient_email = patient_credentials.get("email")
        generate_otp = f"{secrets.randbelow(1_000_000):06d}"
        try:
            store_otp, status_code = self.otp.insert_otp(patient_email, generate_otp)
            if status_code != 201:
                return {'message': 'Could not generate otp. Please try again.'}, 500
            message = Message(subject="Healthcare Portal - Otp verification",
                              recipients=[patient_email],
                              body=f"""Hello,
                            Your Otp for medical records access is :{generate_otp}.\n\n
                            This Otp is valid for 60 minutes.\n 
                            Do not share it with unauthorized person.""")
            mail.send(message)
            return {'message': "Otp sent to your registered email."}, 200
        except Exception:
            current_app.logger.exception('Failed to create or send to your registered mail.')
            return {
                "message": "Unable to send OTP. Please try again."
            }, 500
