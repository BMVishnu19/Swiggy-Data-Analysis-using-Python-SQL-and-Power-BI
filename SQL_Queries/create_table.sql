CREATE TABLE swiggy_restaurants (
    id INT,
    area VARCHAR(100),
    city VARCHAR(50),
    restaurant VARCHAR(200),
    price NUMERIC,
    avg_ratings NUMERIC,
    total_ratings INT,
    food_type TEXT,
    address TEXT,
    delivery_time INT,
    rating_band VARCHAR(20),
    price_category VARCHAR(20),
    delivery_performance VARCHAR(20),
    cuisine_count INT,
    high_value_flag BOOLEAN
);

SELECT * FROM swiggy_restaurants LIMIT 5;
