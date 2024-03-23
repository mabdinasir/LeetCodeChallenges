Query the two cities in STATION with the shortest and longest CITY names, as well as their 
respective lengths (i.e.: number of characters in the name). 
If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

The STATION table is described as follows:

+-------------+----------+
| Field       | Type     |
+-------------+----------+
| ID          | INT      |
| CITY        | VARCHAR(21)|
| STATE       | VARCHAR(2) |
| LAT_N       | NUMERIC  |
| LONG_W      | NUMERIC  |
+-------------+----------+

where LAT_N is the northern latitude and LONG_W is the western longitude.

--Solution
SELECT city, LENGTH(city) FROM station
ORDER BY LENGTH(city) ASC, city ASC
LIMIT 1;

SELECT city, LENGTH(city) FROM station
ORDER BY LENGTH(city) DESC, city ASC
LIMIT 1;