import pandas as pd
import numpy as np

# --------------------------------------------
# Loading the Dataset
# --------------------------------------------
file_path = "C:/Users/Vishnu B M/Documents/Power BI Projects/Case Study Projects/Swiggy Data Analysis Project/archive (4)/swiggy.csv"
df = pd.read_csv(file_path)

print("Initial Dataset Shape:", df.shape)
print(df.head())

# --------------------------------------------
# Standardization of the Column Names
# --------------------------------------------
df.columns = df.columns.str.lower().str.replace(" ", "_")

print("\nColumn Names After Standardization:")
print(df.columns)

# --------------------------------------------
# Data Type Validation
# --------------------------------------------
print("\nData Types:")
print(df.dtypes)

# --------------------------------------------
# Checking the Duplicate Records
# --------------------------------------------
duplicate_count = df.duplicated().sum()
print("\nDuplicate Records:", duplicate_count)

if duplicate_count > 0:
    df = df.drop_duplicates()
    print("Duplicates removed.")

# --------------------------------------------
# Checking the Missing Values
# --------------------------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# --------------------------------------------
#  Rating Validation
# --------------------------------------------
print("\nRating Statistics:")
print(df['avg_ratings'].describe())

# Removal of unrealistic ratings
df = df[df['avg_ratings'] >= 1]

# --------------------------------------------
#  Price Validation
# --------------------------------------------
df = df[df['price'] > 0]

# --------------------------------------------
#  Trimming Text Columns
# --------------------------------------------
text_columns = ['area', 'city', 'restaurant', 'food_type', 'address']

for col in text_columns:
    df[col] = df[col].str.strip()

# --------------------------------------------
# Save Cleaned Dataset
# --------------------------------------------
output_path = "../swiggy_cleaned_dataset.csv"
df.to_csv(output_path, index=False)

print("\nCleaned Dataset Shape:", df.shape)
print("Cleaned file saved to: ", output_path)
