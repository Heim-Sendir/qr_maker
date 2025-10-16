import base64
import os

from src.utils.qr_utils import create_custom_qr
from src.utils.file_utils import FileManager


class QRGenerator:
    BASE_URL = 'https://beepul.uz/actions/payment?qr=2&'

    def __init__(self, output_dir='output'):
        self.fm = FileManager()
        self.output_dir = output_dir

    def generate_url(self, merchant, return_img=False):
        raw_data = f'm={merchant.merchant_id}&cr=860'
        encoded_data = base64.b64encode(raw_data.encode()).decode()
        merchant.url = self.BASE_URL + encoded_data

        qr_img = create_custom_qr(merchant.url)
        if return_img:
            return qr_img
        output_dir = self.fm.get_today_folder()

        qr_path = os.path.join(output_dir, f'{merchant.name}.png')
        qr_img.save(qr_path)
        print(f'✅ QR сохранён: {qr_path}')
