import pandas as pd

# ---------------------------------------
# Loading the Cleaned Dataset
# ---------------------------------------

df = pd.read_csv("C:/Users/Vishnu B M/Documents/Power BI Projects/Case Study Projects/Swiggy Data Analysis Project/swiggy_cleaned_dataset.csv")
print("Initial Dataset Shape:", df.shape)

# ---------------------------------------
# Rating Band Feature
# ---------------------------------------
# Business logic:
# < 3.0   -> Low Rated
# 3.0–4.0 -> Average Rated
# > 4.0   -> High Rated

def rating_band(rating):
    if rating < 3.0:
        return "Low"
    elif rating <= 4.0:
        return "Medium"
    else:
        return "High"

df["rating_band"] = df["avg_ratings"].apply(rating_band)

print("\nRating Band Distribution:")
print(df["rating_band"].value_counts())

# ---------------------------------------
# Price Category Feature
# ---------------------------------------
# Business logic (₹):
# <= 250     -> Budget
# 251–500   -> Mid-range
# > 500     -> Premium

def price_category(price):
    if price <= 250:
        return "Budget"
    elif price <= 500:
        return "Mid-range"
    else:
        return "Premium"

df["price_category"] = df["price"].apply(price_category)

print("\nPrice Category Distribution:")
print(df["price_category"].value_counts())

# ---------------------------------------
# Delivery Performance Feature
# ---------------------------------------
# Business logic:
# <= 45 mins -> Fast
# 46–60     -> Normal
# > 60      -> Slow

def delivery_performance(time):
    if time <= 45:
        return "Fast"
    elif time <= 60:
        return "Normal"
    else:
        return "Slow"

df["delivery_performance"] = df["delivery_time"].apply(delivery_performance)

print("\nDelivery Performance Distribution:")
print(df["delivery_performance"].value_counts())

# ---------------------------------------
# Cuisine Count Feature
# ---------------------------------------
# Number of cuisines served by a restaurant

df["cuisine_count"] = df["food_type"].apply(
    lambda x: len(x.split(","))
)

print("\nCuisine Count Summary:")
print(df["cuisine_count"].describe())

# ---------------------------------------
# High-Value Restaurant Flag
# ---------------------------------------
# High rating + Budget or Mid-range pricing

df["high_value_flag"] = (
    (df["rating_band"] == "High") &
    (df["price_category"].isin(["Budget", "Mid-range"]))
)

print("\nHigh Value Restaurants Count:")
print(df["high_value_flag"].value_counts())

# ---------------------------------------
# Save Feature Engineered Dataset
# ---------------------------------------

output_path = "../swiggy_feature_engineered_dataset.csv"
df.to_csv(output_path, index=False)

print("\nFeature Engineered Dataset Shape:", df.shape)
print("File saved to:", output_path)
print("\nPhase-4 Feature Engineering Completed Successfully.")
