import base64
import os

from PIL import Image
from src.utils.qr_utils import create_custom_qr
from src.utils.file_utils import FileManager


class QRGenerator:
    BASE_URL = 'https://beepul.uz/actions/payment?qr=2&'

    def __init__(self, output_dir='output'):
        self.fm = FileManager()
        self.output_dir = output_dir

    def _build_url(self, merchant_id: str) -> str:
        raw_data = f'm={merchant_id}&cr=860'
        encoded_data = base64.b64encode(raw_data.encode()).decode()
        return self.BASE_URL + encoded_data

    def _buidl_qr(self, data: str, size: int = 20, border: int = 4):
        return create_custom_qr(data, size=size, border=border)

    def generate_url(self, merchant, return_img=False):
        merchant.url = self._build_url(merchant.merchant_id)
        qr_img = self._buidl_qr(merchant.url)

        if return_img:
            return qr_img
        output_dir = self.fm.get_today_folder()

        qr_path = os.path.join(output_dir, f'{merchant.name}.png')
        qr_img.save(qr_path)
        print(f'✅ QR сохранён: {qr_path}')

    def generate_url_with_template(self, merchant):
        merchant.url = self._build_url(merchant.merchant_id)
        qr_img = self._buidl_qr(merchant.url, size=9, border=1)
        qr_img = qr_img.resize((414, 414), Image.LANCZOS)
        print(f'✅ QR сохранён: {merchant.name}')
        return qr_img
