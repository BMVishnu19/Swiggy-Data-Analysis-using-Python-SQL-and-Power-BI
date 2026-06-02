SELECT price_category, ROUND(AVG(avg_ratings), 2) AS avg_rating
FROM swiggy_restaurants
GROUP BY price_category;
