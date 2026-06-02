SELECT restaurant, city, price, avg_ratings
FROM swiggy_restaurants
WHERE price_category = 'Budget'
  AND rating_band = 'High'
ORDER BY avg_ratings DESC;
