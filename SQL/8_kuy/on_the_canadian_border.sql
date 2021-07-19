SELECT *
FROM travelers
WHERE country != "Canada"
    and country != "Mexico"
    and country != "USA";

-- SELECT name, country FROM travelers WHERE country NOT IN ('Canada', 'Mexico', 'USA');
