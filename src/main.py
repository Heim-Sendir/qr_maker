import argparse

from src.utils.file_utils import FileManager
from src.services.qr_generator import QRGenerator


# def main():
#     fm = FileManager()
#     qr = QRGenerator()

#     merchants = fm.read_merchants("data/merchants.csv")

#     for m in merchants:
#         qr.generate_url(m)

#     parser = argparse.ArgumentParser(description="QR Generator Tool")
#     parser.add_argument(
#         '--qr',
#         action='store_true',
#         help='Генерация QR-кодов без шаблона'
#     )

#     parser.add_a

def main():
    parser = argparse.ArgumentParser(description='QR Generator Tool')
    parser.add_argument(
        '--qr',
        action='store_true',
        help='Генерация QR-кодов без шаблона'
    )
    parser.add_argument(
        '--template',
        action='store_true',
        help='Генерация QR-кодов с шаблоном'
    )
    parser.add_argument(
        '--clean',
        action='store_true',
        help='Очистка выходной директории output'
    )

    args = parser.parse_args()

    fm = FileManager()

    if args.qr:
        print('🧩 Режим: генерация QR')
        qr = QRGenerator()
        merchants = fm.read_merchants('data/merchants.csv')

        for m in merchants:
            qr.generate_url(m)
        print('✅ QR-коды успешно сгенерированы!')

    elif args.template:
        print('🖼️ Режим: генерация QR + шаблон')
        pass

    elif args.clean:
        print("🧹 Режим: очистка папки output")
        fm.clear_output()
        print("✅ Папка output очищена")

    else:
        print("❌ Ошибка: укажите режим работы --qr, --template или --clean")


if __name__ == "__main__":
    main()
