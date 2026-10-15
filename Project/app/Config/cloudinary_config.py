import cloudinary.uploader
import certifi
import ssl
import os
from dotenv import load_dotenv

ssl_context = ssl.create_default_context(cafile=certifi.where())
load_dotenv()
cloudinary.config(
    cloud_name="dofbbfgg4",
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    # api_key="596269484844184",
    api_secret=os.getenv("CLOUDINARY_API_SECRET_KEY"),
    # api_secret="0uzI8tt4-bGFwAZuTfOiEMEQD2o",
    secure=True
)
