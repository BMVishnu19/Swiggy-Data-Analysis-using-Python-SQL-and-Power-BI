SELECT restaurant, city, price, avg_ratings
FROM swiggy_restaurants
WHERE high_value_flag = TRUE
ORDER BY avg_ratings DESC
LIMIT 10;
