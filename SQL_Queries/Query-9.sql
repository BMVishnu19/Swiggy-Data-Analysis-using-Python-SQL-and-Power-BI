SELECT delivery_performance, ROUND(AVG(avg_ratings), 2) AS avg_rating
FROM swiggy_restaurants
GROUP BY delivery_performance;
