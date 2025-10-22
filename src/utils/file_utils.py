import os
import csv
import json

from datetime import datetime
from src.models.merchant import Merchant
from src.config import OUTPUT_DIR_TEST, OUTPUT_DIR_PROD


class FileManager:
    def __init__(self, base_output=OUTPUT_DIR_TEST):
        self.base_output = base_output

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
        if os.path.exists(self.base_output):
            for root, dirs, files in os.walk(self.base_output, topdown=False):
                for file in files:
                    os.remove(os.path.join(root, file))
                for dir_ in dirs:
                    os.rmdir(os.path.join(root, dir_))
        else:
            print(f'⚠️ Папка {self.base_output} не найдена')
