CREATE TABLE IF NOT EXISTS fruits (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    calories DECIMAL,
    fat DECIMAL,
    sugar DECIMAL,
    carbohydrates DECIMAL,
    protein DECIMAL
);