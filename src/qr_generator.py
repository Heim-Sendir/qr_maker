import base64
import os
import qrcode

from datetime import datetime


class QRGenerator:
    BASE_URL = 'https://beepul.uz/actions/payment?qr=2&'

    def __init__(self, output_dir='output'):
        self.output_dir = output_dir

    def _generate_encoded_data(self, merchant_id: str) -> str:
        raw_data = f'm={merchant_id}&cr=860'
        print(raw_data)
        encoded = base64.b64encode(raw_data.encode('utf-8')).decode('utf-8')
        print(encoded)
        return encoded

    def _build_full_url(self, merchant_id: str) -> str:
        encoded = self._generate_encoded_data(merchant_id)
        return f'{self.BASE_URL}{encoded}'

    def _get_today_dir(self) -> str:
        today = datetime.now().strftime("%d.%m.%y")
        full_path = os.path.join(self.output_dir, today)
        os.makedirs(full_path, exist_ok=True)
        return full_path

    def generate_url(self, merchant):
        merchant.url = self._build_full_url(merchant.merchant_id)

        qr_img = qrcode.make(merchant.url)

        output_dir = self._get_today_dir()
        file_path = os.path.join(output_dir, f'{merchant.name}.png')

        qr_img.save(file_path)
        merchant.qr_code_path = file_path

        with open(file_path, 'rb') as f:
            merchant.qr_code_base64 = base64.b64encode(f.read()).decode('utf-8')

        print (f'[+] QR создан для {merchant.name}')
