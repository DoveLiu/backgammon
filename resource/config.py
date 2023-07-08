import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    ROBOT_MAIL_ACCOUNT = os.environ["ROBOT_MAIL_ACCOUNT"]
    ROBOT_MAIL_PASSWORD = os.environ["ROBOT_MAIL_PASSWORD"]
