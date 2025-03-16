import pandas as pd

# Set option to display all columns
pd.set_option('display.max_columns', None)

# Load the CSV file
df = pd.read_csv('water_quality/water_potability.csv')

# Display the first few rows before cleaning
print("Before data cleaning:")
print(df.head(10))

# Data cleaning:

# Fill missing values in 'ph' column with the mean of the column
df['ph'] = df['ph'].fillna(df['ph'].mean())

# Fill missing values in other numeric columns with the mean of each column
df['Hardness'] = df['Hardness'].fillna(df['Hardness'].mean())
df['Solids'] = df['Solids'].fillna(df['Solids'].mean())
df['Chloramines'] = df['Chloramines'].fillna(df['Chloramines'].mean())
df['Sulfate'] = df['Sulfate'].fillna(df['Sulfate'].mean())
df['Conductivity'] = df['Conductivity'].fillna(df['Conductivity'].mean())
df['Organic_carbon'] = df['Organic_carbon'].fillna(df['Organic_carbon'].mean())
df['Trihalomethanes'] = df['Trihalomethanes'].fillna(df['Trihalomethanes'].mean())
df['Turbidity'] = df['Turbidity'].fillna(df['Turbidity'].mean())

# Fill missing values in the 'Potability' column with 0 if necessary
df['Potability'] = df['Potability'].fillna(0)

# Convert 'Potability' column to integer type
df['Potability'] = df['Potability'].astype(int)

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_water_quality.csv', index=False)

# Display the first few rows after cleaning
print("\nAfter data cleaning:")
print(df.head(10))
