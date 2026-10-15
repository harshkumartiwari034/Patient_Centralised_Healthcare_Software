from flask_smorest import Blueprint
from flask import render_template

blp = Blueprint('render template route', __name__, description="all render template route here...")

"------------------------------------PATIENT ROUTE-------------------------------------"


@blp.route('/patient/registration')
def patient_login_page():
    return render_template("Patient/registration.html")


@blp.route('/patient/login')
def patient_login_page():
    return render_template("Patient/login.html")


@blp.route('/patient/dashboard')
def patient_login_page():
    return render_template("Patient/patient_dashboard.html")


@blp.route('/patient/medical_data')
def patient_login_page():
    return render_template("Patient/medical_data.html")


@blp.route('/profile')
def patient_login_page():
    return render_template("Patient/profile.html")


@blp.route('/emergency')
def patient_login_page():
    return render_template("Patient/emergency.html")


@blp.route('/health_card')
def patient_login_page():
    return render_template("Patient/health_card.html")


@blp.route('/record_detail')
def patient_login_page():
    return render_template("Patient/record_details.html")


@blp.route('/test_report')
def patient_login_page():
    return render_template("Patient/test_report_view.html")


@blp.route('/language')
def patient_login_page():
    return render_template("Patient/language.html")


@blp.route('/help')
def patient_login_page():
    return render_template("Patient/help.html")


"----------------------------------DOCTOR ROUTE----------------------------------------"


@blp.route('/doctor/registration')
def patient_login_page():
    return render_template("Doctor/registration.html")


@blp.route('/doctor/login')
def patient_login_page():
    return render_template("Doctor/doctor_login.html")


@blp.route('/doctor/dashboard')
def patient_login_page():
    return render_template("Doctor/dashboard.html")


@blp.route('/doctor/emergency')
def patient_login_page():
    return render_template("Doctor/emergency.html")


@blp.route('/doctor/add_medical_records')
def patient_login_page():
    return render_template("Doctor/add_medical_records.html")


@blp.route('/doctor/profile')
def patient_login_page():
    return render_template("Doctor/profile.html")


@blp.route('/doctor/patient')
def patient_login_page():
    return render_template("Doctor/patient.html")


@blp.route('/doctor/medical_records')
def patient_login_page():
    return render_template("Doctor/medical_records.html")


@blp.route('/doctor/medical_reports')
def patient_login_page():
    return render_template("Doctor/medical_reports.html")
