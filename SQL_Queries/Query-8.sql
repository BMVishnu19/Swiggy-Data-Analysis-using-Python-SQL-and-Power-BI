SELECT city, ROUND(AVG(delivery_time), 2) AS avg_delivery_time
FROM swiggy_restaurants
GROUP BY city
ORDER BY avg_delivery_time;
