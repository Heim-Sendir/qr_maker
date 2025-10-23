import os

from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parents[1] / '.env'
load_dotenv(env_path)

BASE_URL = str(os.getenv('BASE_URL'))
CR_VALUE = str(os.getenv('CR_VALUE'))
OUTPUT_DIR_PROD = str(os.getenv('OUTPUT_DIR_PROD'))
OUTPUT_DIR_DEV = str(os.getenv('OUTPUT_DIR_DEV'))
QR_BOX_SIZE = int(os.getenv('QR_BOX_SIZE'))
QR_BOX_SIZE_SMALL = int(os.getenv('QR_BOX_SIZE_SMALL'))
QR_BORDER = int(os.getenv('QR_BORDER'))
QR_BORDER_SMALL = int(os.getenv('QR_BORDER_SMALL'))
RESIZE_IMG = tuple(map(int, os.getenv('RESIZE_IMG').split(',')))
FILL_COLOR = str(os.getenv('FILL_COLOR'))
BACK_COLOR = str(os.getenv('BACK_COLOR'))
