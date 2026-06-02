SELECT city, COUNT(*) AS high_value_count
FROM swiggy_restaurants
WHERE high_value_flag = TRUE
GROUP BY city
ORDER BY high_value_count DESC;
