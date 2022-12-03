2.3.2.1
SELECT COUNT(*)
FROM
    sql.teams, /*таблица с командами*/
    sql.matches /*таблица с матчами*/

2.3.2.2
SELECT 
    long_name,
    home_team_goals,
    away_team_goals
    
FROM
    sql.teams, /*таблица с командами*/
    sql.matches /*таблица с матчами*/
WHERE home_team_api_id = api_id /*условие: home_team_api_id таблицы matches равен api_id таблицы teams*/

2.3.3.1
SELECT *
FROM
    sql.teams
JOIN sql.matches ON away_team_api_id = api_id


2.3.3.2
SELECT 
    matches.id AS match_id,
    teams.id AS team_id
from
    sql.matches
JOIN sql.teams ON home_team_api_id = api_id




2.4.1.1.1
/*city, customer, driver, shipment, truck*/
SELECT *
from sql.city
JOIN shipment ON city.city_id = shipment.city_id
ORDER BY weight DESC

2.4.1.1.2
/*city, customer, driver, shipment, truck*/
SELECT DISTINCT make
from sql.truck

2.4.1.1.3
/*city, customer, driver, shipment, truck*/
SELECT 
    driver.first_name AS name,
    shipment.cust_id AS c_id,
    COUNT(*) AS count_s
from sql.shipment
    JOIN driver ON shipment.driver_id = driver.driver_id
GROUP BY name, c_id
ORDER BY count_s DESC

2.4.1.1.4
/*city, customer, driver, shipment, truck*/
SELECT *
from sql.shipment
ORDER BY ship_date DESC


2.4.1.1.5
/*city, customer, driver, shipment, truck*/
SELECT 
    cust_name,
    COUNT(*) AS count_ship
from sql.customer
JOIN sql.shipment ON customer.cust_id = shipment.cust_id
WHERE ship_date >= to_date('01.01.2017','dd.mm.yyyy')
GROUP BY cust_name
ORDER BY count_ship DESC

2.4.2.1
/*city, customer, driver, shipment, truck*/
SELECT
         c.city_name AS object_name, 'city' AS object_type
FROM 
         sql.city AS c

UNION ALL

SELECT
         c.state, 'state'
FROM 
         sql.city AS c

UNION ALL

SELECT
        d.first_name, 'driver'
FROM 
        sql.driver AS d

UNION ALL

SELECT
        t.make, 'truck'
FROM 
        sql.truck AS t
        
ORDER BY object_name, object_type

2.4.2.2
/*city, customer, driver, shipment, truck*/
SELECT
         c.city_name AS object_name, 'city' AS object_type
FROM 
         sql.city AS c

UNION ALL

SELECT
         c.state, 'state'
FROM 
         sql.city AS c
ORDER BY object_name


2.4.2.3.
/*city, customer, driver, shipment, truck*/
SELECT DISTINCT
        c.city_name AS object_name, 'city' AS object_type
FROM 
        sql.city AS c

UNION ALL

SELECT DISTINCT
        c.state, 'state'
FROM 
        sql.city AS c
ORDER BY object_name


2.4.3.1
/*city, customer, driver, shipment, truck*/
SELECT 
    first_name AS object_name,
    zip_code::text AS contact,
    'zip' AS object_type
from sql.driver

UNION all

SELECT 
    first_name AS object_name,
    phone::text AS contact,
    'phone' AS object_type
from sql.driver

ORDER BY contact, object_name


2.4.4.1
/*city, customer, driver, shipment, truck*/
SELECT 
    ship_date::text AS date_period,
    COUNT(*)::text AS cnt_shipping
    
from sql.shipment
GROUP BY ship_date


UNION all

SELECT 
    'total_shipment'::text,
    SUM(ship_id)::text
from sql.shipment

ORDER BY date_period DESC
















