2.1
/*Найдем максимальный возраст*/
SELECT 
    'max_age' AS "Парамерт",
    max(age) AS "Значение"
FROM hh.candidate

2.2


2.3
/*hh.candidate hh.city hh.candidate_timetable_type hh.timetable_type*/
SELECT 
    age AS "Возраст соискателей",
    COUNT(*) AS "Число соискателей данного возраста"
    
from hh.candidate
GROUP BY age
ORDER BY age DESC


2.4
/*hh.candidate hh.city hh.candidate_timetable_type hh.timetable_type*/
SELECT 
    COUNT(*) AS "Число соискателей данного возраста"
    
from hh.candidate
WHERE age > 40 AND age < 100

3.1
/*hh.candidate hh.city hh.candidate_timetable_type hh.timetable_type*/
SELECT 
    title AS "Город",
    COUNT(*) AS "Число_соискателей"
    
from hh.candidate AS cand
    JOIN hh.city ON cand.city_id = city.id
GROUP BY Город
ORDER BY Число_соискателей DESC

3.2
/*hh.candidate hh.city hh.candidate_timetable_type hh.timetable_type*/
SELECT 
    gender AS "Пол",
    age AS "Возраст",
    desirable_occupation AS "Желаемая_должность",
    city.title AS "Город",
    employment_type AS "Занятость"
    
from hh.candidate AS cand
    JOIN hh.city ON cand.city_id = city.id
WHERE city.title = 'Москва' AND employment_type LIKE '%проектная работа%'
ORDER BY cand.id

3.3
/*hh.candidate hh.city hh.candidate_timetable_type hh.timetable_type*/
SELECT 
    gender AS "Пол",
    age AS "Возраст",
    desirable_occupation AS "Желаемая_должность",
    city.title AS "Город",
    employment_type AS "Занятость"    
from hh.candidate AS cand
    JOIN hh.city ON cand.city_id = city.id
WHERE age < 100
    AND city.title = 'Москва' 
    AND employment_type LIKE '%проектная работа%'
    AND(lower (desirable_occupation) LIKE '%разработчик%'
    OR lower (desirable_occupation) LIKE '%аналитик%'
    OR lower (desirable_occupation) LIKE '%программист%')
ORDER BY city.title, cand.id

3.4
/*hh.candidate hh.city hh.candidate_timetable_type hh.timetable_type*/
SELECT 
    cand.id AS "Номер",
    city.title AS "Город"
    
from hh.candidate AS cand
    JOIN hh.city ON cand.city_id = city.id
WHERE desirable_occupation = current_occupation
ORDER BY city.title, cand.id

3.5
SELECT 
    'Число соискателей старше 40 лет' AS "Параметр",
    COUNT(*) AS "Значение"
from hh.candidate
WHERE age < 100 AND (gender = 'M' AND age >= 65) OR (gender = 'F' AND age >= 60)


4.1
/*hh.candidate hh.city hh.candidate_timetable_type hh.timetable_type*/
SELECT 
    gender AS "Пол",
    age AS "Возраст",
    desirable_occupation AS "Желаемая_должность",
    city.title AS "Город",
    employment_type AS "Занятость",
    timetable_type.title AS "График"
    
from hh.candidate AS cand
    JOIN hh.city ON cand.city_id = city.id
    JOIN hh.candidate_timetable_type ON candidate_timetable_type.candidate_id = cand.id
    JOIN hh.timetable_type ON timetable_type.id = candidate_timetable_type.timetable_id

WHERE age < 100 
    AND (city.title = 'Новосибирск'
    OR city.title = 'Омск'
    OR city.title = 'Томск'
    OR city.title = 'Тюмень')
    AND timetable_type.title = 'вахтовый метод'
    
ORDER BY city.title, cand.id

4.2
/*
Для добывающей компании нам необходимо подобрать кандидатов из Новосибирска, Омска, Томска и Тюмени, которые готовы работать вахтовым методом.
Формат выборки: gender, age, desirable_occupation, city, employment_type, timetable_type.
Отсортируйте результат по городу и номеру кандидата.*/
/*hh.candidate hh.city hh.candidate_timetable_type hh.timetable_type*/
(SELECT 
    desirable_occupation::text,
    age
    
from hh.candidate AS cand
    JOIN hh.city ON cand.city_id = city.id

WHERE age between 16 and 21
    AND city.title = 'Санкт-Петербург'
ORDER BY age
LIMIT 10)

UNION ALL

(SELECT 
    'Total'::text,
    COUNT(age)
from hh.candidate AS cand
    JOIN hh.city ON cand.city_id = city.id
WHERE age between 16 and 21
    AND city.title = 'Санкт-Петербург')


Attestation 2

4
/*sqlprotest.movies sqlprotest.movie_genres sqlprotest.genres*/
SELECT
    genres.name AS genre_name,
    COUNT(*) AS movies_count
FROM sqlprotest.movies
    join sqlprotest.movie_genres ON movies.id = movie_genres.movie_id
    join sqlprotest.genres ON movie_genres.genre_id = genres.id
GROUP BY genre_name 
HAVING COUNT(*) >= 3
ORDER BY movies_count DESC


5
SELECT 
    name,
    description
FROM A

UNION

SELECT 
    name,
    description
FROM B

8
SELECT
    movies.id,
    movies.name,
    movies.year,
    movies.rating
FROM sqlprotest.movies

EXCEPT

SELECT
    movies.id,
    movies.name,
    movies.year,
    movies.rating
FROM sqlprotest.movies
    join sqlprotest.movie_genres ON movies.id = movie_genres.movie_id
    join sqlprotest.genres ON movie_genres.genre_id = genres.id
WHERE genres.name = 'Криминал'
ORDER BY 2

9
SELECT *
FROM sqlprotest.movies
WHERE rating IS NOT NULL
ORDER BY year
LIMIT 3


12
SELECT 
    name,
    COALESCE(rating,0)
FROM sqlprotest.movies






