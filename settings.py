from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    token = os.getenv("TG_TOKEN")


settings = Settings()
