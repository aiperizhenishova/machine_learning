import pandas as pd

# Load the CSV file
df = pd.read_csv('water_quality/cafe_sales.csv')

# Clean the data

# Replace 'ERROR' with NaN and handle missing values
df['Total Spent'] = pd.to_numeric(df['Total Spent'], errors='coerce')

# Replace 'UNKNOWN' and empty strings with 'Unknown'
df['Item'] = df['Item'].replace('UNKNOWN', 'Unknown').fillna('Unknown')
df['Location'] = df['Location'].replace('UNKNOWN', 'Unknown').fillna('Unknown')
df['Payment Method'] = df['Payment Method'].replace('ERROR', 'Unknown').fillna('Unknown')

# Convert the 'Transaction Date' column to datetime format
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')

# Display data before and after cleaning
print("Before data cleaning:")
print(df.head(10))  # Show only the first 10 rows for example

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_transactions.csv', index=False)

print("\nAfter data cleaning:")
print(df.head(10))
