import pandas as pd


pd.set_option('display.max_columns', None)


df = pd.read_csv('water_quality/water_potability.csv')

# Выведем первые строки для анализа
print("Before data cleaning:")
print(df.head(10))


# Заменим пустые значения (NaN) на средние значения для числовых столбцов
df['Hardness'] = df['Hardness'].fillna(df['Hardness'].mean())
df['Solids'] = df['Solids'].fillna(df['Solids'].mean())
df['Chloramines'] = df['Chloramines'].fillna(df['Chloramines'].mean())
df['Sulfate'] = df['Sulfate'].fillna(df['Sulfate'].mean())
df['Conductivity'] = df['Conductivity'].fillna(df['Conductivity'].mean())
df['Organic_carbon'] = df['Organic_carbon'].fillna(df['Organic_carbon'].mean())
df['Trihalomethanes'] = df['Trihalomethanes'].fillna(
    df['Trihalomethanes'].mean())
df['Turbidity'] = df['Turbidity'].fillna(df['Turbidity'].mean())

df['Potability'] = df['Potability'].fillna(0)

# Преобразуем столбец 'Potability' в целочисленный тип
df['Potability'] = df['Potability'].astype(int)

# Сохраним очищенные данные в новый CSV файл
df.to_csv('cleaned_water_quality.csv', index=False)

print("\nAfter data cleaning:")
print(df.head(10))
