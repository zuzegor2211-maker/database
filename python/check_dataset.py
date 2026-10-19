import pandas as pd

# Укажи точное имя скачанного файла
FILE_PATH = "loan.csv"  # или путь к файлу, если он лежит в другом месте

def main():
    print("Загрузка датасета... (может занять 20-40 секунд из-за размера)")
    
    # Читаем датасет
    df = pd.read_csv(FILE_PATH, low_memory=False)
    
    row_count = len(df)
    col_count = len(df.columns)
    
    print("=" * 50)
    print(f"Количество строк: {row_count:,}")
    print(f"Количество колонок: {col_count}")
    print(f"Проверка условия (>= 1,000,000 строк): {'ПРОЙДЕНА ✅' if row_count >= 1_000_000 else 'НЕ ПРОЙДЕНА ❌'}")
    print("=" * 50)
    
    # Сохраняем список колонок в папку для аналитика
    output_file = "../docs/analysis/dataset_columns.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Всего строк: {row_count}\n")
        f.write(f"Всего колонок: {col_count}\n\n")
        f.write("Список всех колонок и их типов данных:\n")
        f.write("-" * 40 + "\n")
        for i, (col, dtype) in enumerate(df.dtypes.items(), 1):
            f.write(f"{i}. {col} ({dtype})\n")
            
    print(f"Список колонок успешно сохранен в {output_file}")

if __name__ == "__main__":
    main()