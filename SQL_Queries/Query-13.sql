SELECT cuisine_count, ROUND(AVG(avg_ratings), 2) AS avg_rating
FROM swiggy_restaurants
GROUP BY cuisine_count
ORDER BY cuisine_count;
