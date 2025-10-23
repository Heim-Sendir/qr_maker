
from tqdm import tqdm
from datetime import datetime

dt = datetime.now().strftime('%d.%m.%y')

class GenerationRunner:
    def __init__(self, fm, report, qr):
        self.fm = fm
        self.report = report
        self.qr = qr
    
    def run(self, merchants, mode: str):
        errors = 0
        report_count = 0
        desc_text = 'Генерация QR-кодов' if mode == 'qr' else 'Генерация QR с шаблоном'

        for m in tqdm(merchants, desc=desc_text, ncols=80):
            try:
                if mode =='qr':
                    self.qr.generate_url(m)
                else:
                    self.qr.generate_url_with_template(m)

                self.report.append({
                    'id': m.merchant_id,
                    'name': m.name,
                    'url': m.url,
                    'qr_path': getattr(m, 'qr_path', None),
                })
                report_count += 1
            except Exception as e:
                errors += 1
                print(f"❌ Ошибка при обработке {m.name}: {e}")
        self._print_summary(mode, report_count, errors)

    def _print_summary(self, mode, report_count, errors):
        print("\n==============================")
        print(f"Сгенерировано QR {'с шаблоном' if mode == 'template' else 'без шаблона'}: {report_count}")
        print(f"Ошибочных: {errors}")
        print(f"Отчёт: {self.fm.get_today_folder()}/{dt}_report.json")
        print("Генерация завершена ✅")
        print("==============================\n")
