import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv('BASE_URL', 'https://the-internet.herokuapp.com')

VALID_USER = os.getenv("VALID_USER")
VALID_PASS = os.getenv("VALID_PASS")

if not VALID_USER or not VALID_PASS:
    raise ValueError("Переменные VALID_USER или VALID_PASS не найдены в .env файле.")
