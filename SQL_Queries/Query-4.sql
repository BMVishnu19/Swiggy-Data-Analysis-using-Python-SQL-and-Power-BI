SELECT city, COUNT(*) AS low_rated_count
FROM swiggy_restaurants
WHERE rating_band = 'Low'
GROUP BY city
ORDER BY low_rated_count DESC;
