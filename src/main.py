import argparse
import os

from src.utils.file_utils import FileManager
from src.services.qr_generator import QRGenerator
from src.services.template_render import TemplateRenderer
from src.services.report_generator import ReportGenerator


def main() -> None:
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
    report = ReportGenerator(fm)

    if args.qr:
        print('🧩 Режим: генерация QR')
        qr = QRGenerator()
        merchants = fm.read_merchants('data/merchants.csv')

        for m in merchants:
            qr.generate_url(m)
            report.append({
                'id': m.merchant_id,
                'name': m.name,
                'url': m.url,
                'qr_path': getattr(m, 'qr_path', None),
            })
        print('✅ QR-коды успешно сгенерированы!')

    elif args.template:
        print('🖼️ Режим: генерация QR + шаблон')

        fm = FileManager()
        qr = QRGenerator()
        merchants = fm.read_merchants('data/merchants.csv')

        template = TemplateRenderer('src/templates/base_template.png')
        positions = [
            (494, 244),
            (494, 700),
            (1515, 244),
            (1515, 700)
            ]
        output_dir = fm.get_today_folder()

        for m in merchants:
            qr_img = qr.generate_url_with_template(m)
            combined = template.place_qr(qr_img, positions)
            output_path = os.path.join(output_dir,
                                       f'{m.name}_template.png')
            combined.save(output_path)
            m.qr_path = output_path
            report.append({
                'id': m.merchant_id,
                'name': m.name,
                'url': m.url,
                'qr_path': getattr(m, 'qr_path', None),
            })

    elif args.clean:
        print('🧹 Режим: очистка папки')
        fm.clear_output()
        print('✅ Папка "output" очищена')

    else:
        print("❌ Ошибка: укажите режим работы --qr, --template или --clean")


if __name__ == "__main__":
    main()
