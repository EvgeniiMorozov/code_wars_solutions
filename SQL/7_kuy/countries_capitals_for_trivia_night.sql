SELECT capital
FROM countries
ORDER BY capital
WHERE country IN ("Africa", "Afrika")
    AND capital LIKE "E"
LIMIT 3;