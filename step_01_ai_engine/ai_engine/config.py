from dataclasses import dataclass
import os

@dataclass
class AIConfig:
    UPLOAD_DIR = os.getenv("UPLOAD_DIR","uploads")
    LOG_LEVEL = os.getenv("LOG_LEVEL","INFO")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL","gpt-4.1-mini")
    OCR_LANGUAGE = "en"
