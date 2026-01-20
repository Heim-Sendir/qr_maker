import base64
import os

from PIL import Image  # type: ignore
from src.utils.qr_utils import create_custom_qr
from src.config import (BASE_URL, CR_VALUE, QR_BOX_SIZE, QR_BORDER,
                        QR_BOX_SIZE_SMALL, QR_BORDER_SMALL, RESIZE_IMG)


class QRGenerator:

    def __init__(self, fm, is_super=False):
        self.fm = fm
        self.is_super = is_super

    def _build_url_default(self, merchant_id: str) -> str:
        raw_data = f'm={merchant_id}&{CR_VALUE}'
        encoded_data = base64.b64encode(raw_data.encode()).decode()
        return BASE_URL + encoded_data

    def _build_url_super(self, merchant_id: str) -> str:
        raw_data = f'i={merchant_id}&{CR_VALUE}'
        encoded_data = base64.b64encode(raw_data.encode()).decode()
        return BASE_URL + encoded_data

    def _build_url(self, merchant_id: str) -> str:
        if self.is_super:
            return self._build_url_super(merchant_id)
        else:
            return self._build_url_default(merchant_id)

    def _build_qr(self, data: str, size: int, border: int):
        return create_custom_qr(data, size=size, border=border)

    def generate_url(self, merchant, return_img=False) -> None:
        merchant.url = self._build_url(merchant.merchant_id)
        qr_img = self._build_qr(merchant.url, QR_BOX_SIZE, QR_BORDER)

        if return_img:
            return qr_img
        output_dir = self.fm.get_today_folder()

        qr_path = os.path.join(output_dir, f'{merchant.name}.png')
        qr_img.save(qr_path)
        merchant.qr_path = qr_path

    def generate_url_with_template(self, merchant) -> Image:
        merchant.url = self._build_url(merchant.merchant_id)
        qr_img = self._build_qr(
            merchant.url,
            QR_BOX_SIZE_SMALL,
            QR_BORDER_SMALL
            )
        qr_img = qr_img.resize(RESIZE_IMG, Image.LANCZOS)
        return qr_img
