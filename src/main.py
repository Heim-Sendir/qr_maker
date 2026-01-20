import argparse

from src.utils.file_utils import FileManager
from src.services.qr_generator import QRGenerator
from src.services.template_render import TemplateRenderer
from src.services.report_generator import ReportGenerator
from src.services.generation_runner import GenerationRunner
from src.config import BASE_FILE_PATH, BASE_TEMPLATE_PATH


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
    parser.add_argument(
        '--dev',
        action='store_true',
        help='Режим разработки - сохраняет файлы в дирректорию output'
    )
    parser.add_argument(
        '--super',
        action='store_true',
        help='Генерация QR кода для супермерчанта'
    )

    args = parser.parse_args()

    fm = FileManager(dev_mode=args.dev)
    report = ReportGenerator(fm)

    if args.qr:

        qr = QRGenerator(fm, is_super=args.super)
        merchants = fm.read_file(BASE_FILE_PATH)
        report = ReportGenerator(fm)
        runner = GenerationRunner(fm, report, qr)
        runner.run(merchants, mode='qr')

    elif args.template:

        qr = QRGenerator(fm)
        merchants = fm.read_file(BASE_FILE_PATH)
        report = ReportGenerator(fm)

        template = TemplateRenderer(BASE_TEMPLATE_PATH)
        positions = [
            (494, 244),
            (494, 700),
            (1515, 244),
            (1515, 700)
            ]

        runner = GenerationRunner(fm, report, qr,
                                  template=template,
                                  positions=positions,
                                  is_super=args.super)
        runner.run(merchants, mode='template')

    elif args.clean:
        print('🧹 Режим: очистка папки')
        fm.clear_output()

    else:
        print("❌ Ошибка: укажите режим работы --qr, --template или --clean")


if __name__ == "__main__":
    main()
