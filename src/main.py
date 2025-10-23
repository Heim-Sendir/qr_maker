import argparse
import os

from src.utils.file_utils import FileManager
from src.services.qr_generator import QRGenerator
from src.services.template_render import TemplateRenderer
from src.services.report_generator import ReportGenerator
from src.services.generation_runner import GenerationRunner


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

        qr = QRGenerator()
        merchants = fm.read_merchants('data/merchants.csv')
        report = ReportGenerator(fm)
        runner = GenerationRunner(fm, report, qr)
        runner.run(merchants, mode='qr')

    elif args.template:

        qr = QRGenerator()
        merchants = fm.read_merchants('data/merchants.csv')
        report = ReportGenerator(fm)

        template = TemplateRenderer('src/templates/base_template.png')
        positions = [
            (494, 244),
            (494, 700),
            (1515, 244),
            (1515, 700)
            ]

        runner = GenerationRunner(fm, report, qr, template=template, positions=positions)
        runner.run(merchants, mode='template')


    elif args.clean:
        print('🧹 Режим: очистка папки')
        fm.clear_output()
        print('✅ Папка "output" очищена')

    else:
        print("❌ Ошибка: укажите режим работы --qr, --template или --clean")


if __name__ == "__main__":
    main()
