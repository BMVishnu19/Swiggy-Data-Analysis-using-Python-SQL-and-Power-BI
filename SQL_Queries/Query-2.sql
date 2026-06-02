SELECT city, ROUND(AVG(avg_ratings),2) AS avg_city_rating
FROM swiggy_restaurants
GROUP BY city
ORDER BY avg_city_rating DESC;
