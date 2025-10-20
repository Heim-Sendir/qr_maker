# 🧩 QR Maker

Инструмент для массовой генерации QR-кодов с автоматическим формированием ссылок и возможностью вставки QR в шаблонное изображение.




## 🚀 Возможности

Чтение списка мерчантов из CSV-файла (id, name)

Генерация уникальных ссылок по шаблону
https://yoursite.com/{base64}

- Создание QR-кодов в PNG-формате
- Автоматическая сортировка по датам (каждый день — отдельная папка)
- Режим вставки QR-кодов в шаблон PNG (4 позиции)
- Очистка выходных файлов через параметр `--clean`




## ⚙️ Установка
```bash
git clone <репозиторий>
cd qr_maker
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```




## 🧰 Структура проекта
<pre>qr_maker/
│
├── src/
│   ├── main.py                 # Точка входа (CLI)
│   ├── data/                   # CSV с мерчантами
│   ├── output/                 # Папка для готовых QR
│   ├── templates/              # PNG шаблон
│   ├── models/merchant.py      # Класс мерчанта
│   ├── services/
│   │   ├── qr_generator.py     # Логика генерации QR
│   │   └── template_render.py  # Вставка QR в шаблон
│   └── utils/
│       ├── file_utils.py       # Работа с файлами и датами
│       └── qr_utils.py         # Генерация QR (Pillow + qrcode)
│
└── requirements.txt</pre>





## 🧩 Использование

Генерация обычных QR - 
`py -m src.main --qr`

Генерация QR в шаблон - 
`py -m src.main --template`

Очистка папки output - 
`py -m src.main --clean`





## 🧱 Формат CSV
<pre>id,name
1234,name1
1234,name2
1234,name3</pre>




## 📦 Результат
После запуска создаётся папка:
<pre>output/16.10.2025/
├── name1.png
├── name2.png
└── name3.png</pre>

или, при шаблонном режиме:

<pre>output/16.10.2025/
├── name1_with_template.png
├── name2_with_template.png
└── name3_with_template.png</pre>


## 📄 Генерация отчета
После генерации QR кодов генерируется отчет в json и помещается в папку с изображениями, где указаны:
<pre>-ID мерчанта
-Наименование мерчанта
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

Если в течении некоторого времени будет использована новая генерация изображений, то отчет дополняется