from src.file_manager import FileManager
from src.qr_generator import QRGenerator

def main():
    fm = FileManager()
    qr = QRGenerator()

    merchants = fm.read_merchants("data/merchants.csv")

    for m in merchants:
        qr.generate_url(m)

if __name__ == "__main__":
    main()
