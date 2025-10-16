import csv
import json
from src.merchant import Merchant


class FileManager:
    def read_merchants(self, csv_path: str) -> list[Merchant]:
        merchants = []
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                merchant = Merchant(
                    merchant_id=row.get("id", "").strip(),
                    name=row.get("name", "").strip(),
                )
                merchants.append(merchant)
        return merchants
    
    def save_report(self, merchants: list[Merchant], output_path: str):
        data = [m.to_dict() for m in merchants]
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

