import base64
import os

from src.utils.qr_utils import create_custom_qr
from src.utils.file_utils import FileManager


class QRGenerator:
    BASE_URL = 'https://beepul.uz/actions/payment?qr=2&'

    def __init__(self, output_dir='output'):
        self.fm = FileManager()

    def generate_url(self, merchant):
        raw_data = f'm={merchant.merchant_id}&cr=860'
        encoded_data = base64.b64encode(raw_data.encode()).decode()
        merchant.url = self.BASE_URL + encoded_data

        qr_img = create_custom_qr(merchant.url)
        output_dir = self.fm.get_today_folder()

        qr_path = os.path.join(output_dir, f'{merchant.name}.png')
        qr_img.save(qr_path)
        print(f'✅ QR сохранён: {qr_path}')
    # def _generate_encoded_data(self, merchant_id: str) -> str:
    #     raw_data = f'm={merchant_id}&cr=860'
    #     encoded = base64.b64encode(raw_data.encode('utf-8')).decode('utf-8')
    #     return encoded

    # def _build_full_url(self, merchant_id: str) -> str:
    #     encoded = self._generate_encoded_data(merchant_id)
    #     return f'{self.BASE_URL}{encoded}'

    # def _get_today_dir(self) -> str:
    #     today = datetime.now().strftime("%d.%m.%y")
    #     full_path = os.path.join(self.output_dir, today)
    #     os.makedirs(full_path, exist_ok=True)
    #     return full_path

    # def _create_custom_qr(self, data: str):
    #     qr = qrcode.QRCode(
    #         version=None,
    #         error_correction=ERROR_CORRECT_H,
    #         box_size=20,
    #         border=4
    #     )

    #     qr.add_data(data)
    #     qr.make(fit=True)

    #     img = qr.make_image(fill_color='black', back_color='white')
    #     return img

    # def generate_url(self, merchant) -> None:
    #     merchant.url = self._build_full_url(merchant.merchant_id)

    #     qr_img = self._create_custom_qr(merchant.url)

    #     output_dir = self._get_today_dir()
    #     file_path = os.path.join(output_dir, f'{merchant.name}.png')

    #     qr_img.save(file_path)
    #     merchant.qr_code_path = file_path

    #     with open(file_path, 'rb') as f:
    #         merchant.qr_code_base64 = (
    #             base64.b64encode(f.read()).decode('utf-8')
    #             )

    #     print(f'[+] QR создан для {merchant.name}')
