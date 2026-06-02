SELECT city, price_category, COUNT(*) AS count
FROM swiggy_restaurants
GROUP BY city, price_category
ORDER BY city, count DESC;
