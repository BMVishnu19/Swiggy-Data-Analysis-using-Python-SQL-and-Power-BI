import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------
# Loading the Cleaned Dataset
# ---------------------------------------

df = pd.read_csv("C:/Users/Vishnu B M/Documents/Power BI Projects/Case Study Projects/Swiggy Data Analysis Project/swiggy_cleaned_dataset.csv")

print("Dataset Shape:", df.shape)
print("\nFirst 5 Records:")
print(df.head())

# ---------------------------------------
# Basic Statistical Overview
# ---------------------------------------

print("\nNumerical Summary:")
print(df.describe())

# ---------------------------------------
# City-wise Distribution of Restaurants
# ----------------------------------------

city_distribution = df["city"].value_counts()

print("\nTop Cities by Number of Restaurants:")
print(city_distribution.head(10))

plt.figure(figsize=(8, 5))
city_distribution.plot(kind="bar")
plt.title("Number of Restaurants by City")
plt.xlabel("City")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# ---------------------------------------
# Ratings Distribution
# ---------------------------------------

plt.figure(figsize=(8, 5))
sns.histplot(df["avg_ratings"], bins=20, kde=True)
plt.title("Distribution of Average Ratings")
plt.xlabel("Average Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ---------------------------------------
# Price Distribution
# ---------------------------------------

plt.figure(figsize=(8, 5))
sns.boxplot(x=df["price"])
plt.title("Price Distribution of Restaurants")
plt.xlabel("Price")
plt.tight_layout()
plt.show()

# ---------------------------------------
# Price vs Ratings Relationship
# ---------------------------------------

plt.figure(figsize=(8, 5))
sns.scatterplot(x="price", y="avg_ratings", data=df)
plt.title("Price vs Average Ratings")
plt.xlabel("Price")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()

# ---------------------------------------
# Delivery Time Analysis
# ---------------------------------------

print("\nDelivery Time Summary:")
print(df["delivery_time"].describe())

plt.figure(figsize=(8, 5))
sns.boxplot(x="delivery_time", data=df)
plt.title("Delivery Time Distribution")
plt.xlabel("Delivery Time (minutes)")
plt.tight_layout()
plt.show()

# ---------------------------------------
# Ratings vs Delivery Time
# ---------------------------------------

plt.figure(figsize=(8, 5))
sns.scatterplot(x="delivery_time", y="avg_ratings", data=df)
plt.title("Delivery Time vs Average Ratings")
plt.xlabel("Delivery Time")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()

# ---------------------------------------
# Food Type Popularity
# ---------------------------------------

food_series = df["food_type"].str.split(",")
food_exploded = food_series.explode().str.strip()

top_foods = food_exploded.value_counts().head(10)

print("\nTop 10 Food Types:")
print(top_foods)

plt.figure(figsize=(8, 5))
top_foods.plot(kind="bar")
plt.title("Top 10 Food Types")
plt.xlabel("Food Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

print("\nEDA Phase Completed Successfully.")
