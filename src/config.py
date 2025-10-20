import os

from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parents[1] / '.env'
load_dotenv(env_path)

BASE_URL = str(os.getenv('BASE_URL'))
CR_VALUE = str(os.getenv('CR_VALUE'))
OUTPUT_DIR = str(os.getenv('OUTPUT_DIR'))
QR_BOX_SIZE = int(os.getenv('QR_BOX_SIZE'))
QR_BOX_SIZE_SMALL = int(os.getenv('QR_BOX_SIZE_SMALL'))
QR_BORDER = int(os.getenv('QR_BORDER'))
QR_BORDER_SMALL = int(os.getenv('QR_BORDER_SMALL'))
