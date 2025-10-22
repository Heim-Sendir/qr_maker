import json

from datetime import datetime
from pathlib import Path


class ReportGenerator:
    def __init__(self, file_manager):
        self.fm = file_manager
    
    def _get_report_path(self) -> Path:
        folder = Path(self.fm.get_today_folder())
        current_date = datetime.now().strftime('%d.%m.%y')
        return folder / f'{current_date}_report.json'

    def append(self, merchant_data: dict) -> None:
        report_path = self._get_report_path()

        merchant_data.setdefault('create_time', datetime.now().isoformat())

        if not report_path.exists():
            data = [merchant_data]
        else:
            try:
                with open(report_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                data = []
            existing_ids = {item.get('id') for item in data}
            if merchant_data.get('id') not in existing_ids:
                data.append(merchant_data)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"📄 Добавлен в отчёт: {merchant_data.get('name')} ({report_path})")
