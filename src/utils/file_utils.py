import os, csv, shutil

from datetime import datetime
from src.models.merchant import Merchant
from src.config import OUTPUT_DIR_DEV, OUTPUT_DIR_PROD


class FileManager:
    def __init__(self, dev_mode=False):
        self.base_output = OUTPUT_DIR_DEV if dev_mode else OUTPUT_DIR_PROD

    def read_merchants(self, csv_path: str) -> list[Merchant]:
        merchants = []
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(base_dir, csv_path)
        with open(csv_path, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                merchants.append(Merchant(row['id'], row['name']))
        return merchants

    def get_today_folder(self) -> str:
        today = datetime.now().strftime('%d.%m.%y')
        path = os.path.join(self.base_output, today)
        os.makedirs(path, exist_ok=True)
        return path

    def clear_output(self) -> None:
        today_folder = self.get_today_folder()

        if os.path.exists(today_folder):
            shutil.rmtree(today_folder)
            print(f'✅ Папка {today_folder} удалена')
        else:
            print(f'⚠️ Папка {today_folder} не найдена')
