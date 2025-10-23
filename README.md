# 🧩 QR Maker

Инструмент для массовой генерации QR-кодов с автоматическим формированием ссылок и возможностью вставки QR в шаблонное изображение.




## 🚀 Возможности

Чтение списка данных из CSV-файла (id, name)

Генерация уникальных ссылок по шаблону
https://yoursite.com/{base64}

- Создание QR-кодов в PNG-формате
- Автоматическая сортировка по датам (каждый день — отдельная дирректория)
- Режим вставки QR-кодов в шаблон PNG (4 позиции)
- Очистка выходных файлов через параметр `--clean`
- Возможность сохранения файлов в dev-дирректорию




## ⚙️ Установка
```bash
git clone
cd qr_maker
python -m venv venv
source venv\Scripts\activate
pip install -r requirements.txt
```




## 🧰 Структура проекта
<pre>qr_maker/
│
├── src/
│   ├── main.py                   # Точка входа (CLI)
│   ├── config.py                 # Файл с конфигурациями
│   ├── data/                     # CSV шаблон
│   ├── output/                   # Директория для готовых QR
│   ├── templates/                # PNG шаблон
│   ├── models/merchant.py        # Класс мерчанта
│   ├── services/
│   │   ├── qr_generator.py       # Логика генерации QR
│   │   ├── template_render.py    # Вставка QR в шаблон
│   │   ├── report_generator.py   # Управление процессом генерации и прогрессом (tqdm)
│   │   └── gerenation_runner.py  # Генерация отчета в json
│   └── utils/
│       ├── file_utils.py         # Работа с файлами и датами
│       └── qr_utils.py           # Генерация QR (Pillow + qrcode)
│
├── requirements.txt
└── .env                          # Файл с константами
</pre>




## 🧩 Использование

Генерация обычных QR - 
```bash
py -m src.main --qr
```

Генерация QR в шаблон - 
```bash
py -m src.main --template
```

Очистка дирректории - 
```bash
py -m src.main --clean
```

Генерация обычных QR в dev-дирректорию - 
```bash
py -m src.main --qr --dev
```

Генерация QR в шаблон в dev-дирректорию - 
```bash
py -m src.main --template --dev
```

Очистка dev-дирректории - 
```bash
py -m src.main --clean --dev
```


## 🧱 Формат CSV
<pre>id,name
1234,name1
1234,name2
1234,name3</pre>




## 📦 Результат
После запуска создаётся папка:
<pre>
output/{current date}/
├── name1.png
├── name2.png
└── name3.png
</pre>

или, при шаблонном режиме:

<pre>
output/{current date}/
├── name1_with_template.png
├── name2_with_template.png
└── name3_with_template.png
</pre>



## 📄 Генерация отчета
После генерации QR кодов генерируется отчет в json и помещается в папку с изображениями, где указаны:
<pre>-ID
-Наименование
-Полный адрес ссылки с base64
-Пусть сохранения файла
-Дата создания файла изображения

Пример:
[
    {
        "id": "1234",
        "name": "name 1",
        "url": "https://yoursite.com/{base64}",
        "qr_path": "output\\{current date}\\name 1.png",
        "create_time": "{current time}"
    }
]
</pre>

Если в течении текущего дня будет использована новая генерация изображений, то отчет дополняется