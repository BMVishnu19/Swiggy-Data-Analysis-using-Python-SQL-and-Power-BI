SELECT
    UNNEST(STRING_TO_ARRAY(food_type, ',')) AS cuisine,
    COUNT(*) AS frequency
FROM swiggy_restaurants
GROUP BY cuisine
ORDER BY frequency DESC
LIMIT 10;
