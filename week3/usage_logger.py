
import os
from pathlib import Path
from datetime import datetime, timezone

from dotenv import load_dotenv
from pymongo import MongoClient


# Load .env from the week3 folder
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env", override=True)


class UsageLogger:

    def __init__(self):

        mongo_uri = os.getenv("MONGODB_URI")

        if not mongo_uri:
            raise ValueError("MONGODB_URI not found in .env")

        self.client = MongoClient(
            mongo_uri,
            serverSelectionTimeoutMS=10000
        )

        # Check MongoDB connection
        self.client.admin.command("ping")

        self.db = self.client["llm_monitoring"]
        self.collection = self.db["api_usage"]

        print("MongoDB connected successfully!")

    def log_call(self, record):

        record["timestamp"] = datetime.now(timezone.utc)

        self.collection.insert_one(record)

        print("Usage successfully saved to MongoDB!")

    def close(self):
        self.client.close()
