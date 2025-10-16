from src.file_manager import FileManager


def main():
    fm = FileManager()
    merchants = fm.read_merchants('data/merchants.csv')

    for m in merchants:
        print(f'{m.name}: {m.url}')

if __name__ == "__main__":
    main()
