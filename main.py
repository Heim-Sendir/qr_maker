import pandas as pd
import base64

# === Настройки ===
BASE_URL = "https://beepul.uz/actions/payment?qr=2&"
CR_VALUE = 860
CSV_PATH = "data/merchants.csv"

# === Шаг 1: чтение CSV ===
def read_merchants(csv_path):
    try:
        df = pd.read_csv(csv_path)
        df = df.dropna(subset=["id", "name"])  # Убираем пустые строки
        return df
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")
        return pd.DataFrame()

# === Шаг 2: генерация base64 и ссылок ===
def generate_link(merchant_id):
    raw = f"m={merchant_id}&cr={CR_VALUE}"
    encoded = base64.urlsafe_b64encode(raw.encode()).decode()
    encoded = encoded.rstrip("=")  # убираем "=", чтобы ссылка была короче
    return BASE_URL + encoded

# === Шаг 3: тестовый запуск ===
def main():
    merchants = read_merchants(CSV_PATH)
    if merchants.empty:
        print("CSV пустой или не найден.")
        return

    for _, row in merchants.iterrows():
        merchant_id = str(row["id"]).strip()
        name = str(row["name"]).strip()

        link = generate_link(merchant_id)
        print(f"{name}: {link}")

if __name__ == "__main__":
    main()
