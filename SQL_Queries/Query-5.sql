SELECT rating_band, ROUND(AVG(price), 2) AS avg_price
FROM swiggy_restaurants
GROUP BY rating_band;
