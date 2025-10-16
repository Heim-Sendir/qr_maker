class Merchant:
    def __init__(self, merchant_id: str, name: str, url: str):
        self.merchant_id = merchant_id
        self.name = name
        self.url = url
        self.qr_code_path = None
        self.qr_code_base64 = None


def to_dict(self):
    return {
        "merchant_id": self.merchant_id,
        "name": self.name,
        "qr_code_path": self.qr_code_path,
        "qr_code_base64": self.qr_code_base64
    }
