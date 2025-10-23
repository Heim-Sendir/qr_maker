
import os

from tqdm import tqdm
from datetime import datetime

dt = datetime.now().strftime('%d.%m.%y')

class GenerationRunner:
    def __init__(self, fm, report, qr, template=None, positions=None):
        self.fm = fm
        self.report = report
        self.qr = qr
        self.template = template
        self.posotions = positions

    def run(self, merchants, mode: str):
        errors = 0
        report_count = 0
        output_dir = self.fm.get_today_folder()

        desc_text = 'Генерация QR-кодов' if mode == 'qr' else 'Генерация QR с шаблоном'

        for m in tqdm(merchants, desc=desc_text, ncols=80):
            try:
                if mode =='qr':
                    self.qr.generate_url(m)

                elif mode == 'template':
                    qr_img = self.qr.generate_url_with_template(m)

                    combined = self.template.place_qr(qr_img, self.posotions)
                    output_path = os.path.join(output_dir, f'{m.name}_template.png')
                    combined.save(output_path)
                    m.qr_path = output_path

                self.report.append({
                    'id': m.merchant_id,
                    'name': m.name,
                    'url': m.url,
                    'qr_path': getattr(m, 'qr_path', None),
                })
                report_count += 1

            except Exception as e:
                errors += 1
                print(f"⚠️ Ошибка при обработке {m.name}: {e}")
                continue

        self._print_summary(mode, report_count, errors)

    def _print_summary(self, mode, report_count, errors):
        print("\n==============================")
        print(f"Сгенерировано QR {'с шаблоном' if mode == 'template' else 'без шаблона'}: {report_count}")
        print(f"Ошибочных: {errors}")
        print(f"Отчёт: {self.fm.get_today_folder()}/{dt}_report.json")
        print("Генерация завершена ✅")
        print("==============================\n")
