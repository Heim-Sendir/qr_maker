import qrcode

from qrcode.constants import ERROR_CORRECT_H


def create_custom_qr(data: str, size: int = 20, border: int = 4):
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,
        box_size=size,
        border=border
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')
    return img
