SELECT
    city,
    ROUND(
        100.0 * SUM(CASE WHEN rating_band = 'High' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS high_rating_percentage
FROM swiggy_restaurants
GROUP BY city;
