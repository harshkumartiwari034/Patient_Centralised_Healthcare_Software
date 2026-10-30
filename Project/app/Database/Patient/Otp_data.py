from datetime import datetime, timezone
from pymongo import MongoClient, ASCENDING
import os


class PatientOtpDatabase:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGODB_URL"))
        self.db = self.client['PatientCentralisedRecordSystem']
        self.collection = self.db['patient-otp']
        self.collection.create_index([("created_at", ASCENDING)], expireAfterSeconds=3600)

    def insert_otp(self, mail_id, otp):
        user_data = {"mail_id": mail_id, "otp": otp, "created_at": datetime.now(timezone.utc), "used": False}
        result = self.collection.insert_one(user_data)
        if result.inserted_id:
            return {"success": True, 'message': 'otp saved successfully..'}, 201
        else:
            return {"success": False, 'message': 'Otp could not be saved..'}, 500
