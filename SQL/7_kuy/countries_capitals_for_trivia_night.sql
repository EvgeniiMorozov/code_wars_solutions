SELECT capital
FROM countries
WHERE country = ("Africa", "Afrika")
    AND capital LIKE "E"
LIMIT 3;