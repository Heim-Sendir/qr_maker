import qrcode

from qrcode.constants import ERROR_CORRECT_H

def create_custom_qr(data: str, size: int, border: int) -> qrcode.image.base.BaseImage:
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


def create_small_qr(data: str, size: int, border: int) -> qrcode.image.base.BaseImage:
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,
        size=size,
        border=border
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')
    return img
