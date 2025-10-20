
class Merchant:
    def __init__(self, merchant_id: str, name: str):
        self.merchant_id = merchant_id
        self.name = name
        self.url = None

    def __repr__(self):
        return f'{self.name}: {self.url}'
