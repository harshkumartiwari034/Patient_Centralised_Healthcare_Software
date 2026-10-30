from pymongo import MongoClient
import os

class PatientDatabase:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGODB_URL"))
        self.db = self.client['PatientCentralisedRecordSystem']
        self.collection = self.db['patient-report-data']

    def insert_lab_report_data(self, patient_id, blood_test=None, urine_test=None, sugar_test=None, thyroid_test=None,
                               lft_tst=None, kft_test=None, x_ray=None, mri_scan=None, ct_scan=None, ultrasound=None,
                               ecg=None,
                               echo=None):
        pass

