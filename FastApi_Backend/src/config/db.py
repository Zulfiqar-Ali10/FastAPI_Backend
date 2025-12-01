import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

MONGO_URL = os.getenv("MONGO_URL")  # Only the variable name
DATABASE_NAME = os.getenv("DATABASE_NAME")  # Only the variable name

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client[DATABASE_NAME]
