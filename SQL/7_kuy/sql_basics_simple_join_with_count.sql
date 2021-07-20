SELECT people.*, COUNT(*) AS toy_count
FROM people
LEFT JOIN toys ON people.id = toys.people_id
GROUP BY 1;