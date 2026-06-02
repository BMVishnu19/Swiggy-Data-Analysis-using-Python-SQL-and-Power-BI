SELECT restaurant, city, delivery_time, avg_ratings
FROM swiggy_restaurants
WHERE delivery_performance = 'Slow'
  AND rating_band = 'Low';
