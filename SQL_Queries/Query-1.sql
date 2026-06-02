SELECT
    COUNT(*) AS total_restaurants,
    ROUND(AVG(avg_ratings), 2) AS avg_platform_rating,
    ROUND(AVG(price), 2) AS avg_price,
    ROUND(AVG(delivery_time), 2) AS avg_delivery_time
FROM swiggy_restaurants;
