from pymongo import MongoClient
import hashlib
import uuid
import os


class StaffDatabase:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGODB_URL"))
        self.db = self.client['PatientCentralisedRecordSystem']
        self.collection = self.db['staff-data']

    def staff_exist(self, email):
        staff_data = self.collection.find_one({"email": email})
        if staff_data:
            return staff_data, 200

