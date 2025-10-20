import base64
import os

from PIL import Image
from src.utils.qr_utils import create_custom_qr
from src.utils.file_utils import FileManager
from src.config import (BASE_URL, CR_VALUE, QR_BOX_SIZE, QR_BORDER,
                        QR_BOX_SIZE_SMALL, QR_BORDER_SMALL, RESIZE_IMG)


class QRGenerator:

    def __init__(self, output_dir='output'):
        self.fm = FileManager()
        self.output_dir = output_dir

    def _build_url(self, merchant_id: str) -> str:
        raw_data = f'm={merchant_id}&{CR_VALUE}'
        encoded_data = base64.b64encode(raw_data.encode()).decode()
        return BASE_URL + encoded_data

    def _buidl_qr(self, data: str, size: int, border: int) -> function:
        return create_custom_qr(data, size=size, border=border)

    def generate_url(self, merchant, return_img=False) -> None:
        merchant.url = self._build_url(merchant.merchant_id)
        qr_img = self._buidl_qr(merchant.url, QR_BOX_SIZE, QR_BORDER)

        if return_img:
            return qr_img
        output_dir = self.fm.get_today_folder()

        qr_path = os.path.join(output_dir, f'{merchant.name}.png')
        qr_img.save(qr_path)
        print(f'✅ QR сохранён: {merchant.name}')

    def generate_url_with_template(self, merchant) -> Image:
        merchant.url = self._build_url(merchant.merchant_id)
        qr_img = self._buidl_qr(merchant.url, QR_BOX_SIZE_SMALL, QR_BORDER_SMALL)
        qr_img = qr_img.resize(RESIZE_IMG, Image.LANCZOS)
        print(f'✅ QR сохранён: {merchant.name}')
        return qr_img
