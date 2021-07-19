SELECT capital
FROM countries
WHERE continent IN ("Africa", "Afrika")
AND country LIKE "E%"
ORDER BY capital
LIMIT 3;

/*
select capital
from countries
where continent like 'Afri_a' and country like 'E%'
order by capital
limit 3;
*/
