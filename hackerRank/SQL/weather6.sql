Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. 
Your result cannot contain duplicates.

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

-- Solution
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[aeiouAEIOU]';


7. Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
-- Solution
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '[aeiouAEIOU]$';

8.Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
-- Solution
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[aeiouAEIOU].*[aeiouAEIOU]$';

9. Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.
-- Solution
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[^aeiouAEIOU]';

10. Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.
-- Solution
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '[^aeiouAEIOU]$';

11. Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
-- Solution
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[^aeiouAEIOU]|[^aeiouAEIOU]$';

12. Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
-- Solution
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[^aeiouAEIOU].*[^aeiouAEIOU]$';

13. Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than 38.7880 and less than 137.2345. Truncate your answer to 4 decimal places.
-- Solution
SELECT ROUND(SUM(LAT_N), 4)
FROM STATION
WHERE LAT_N > 38.7880 AND LAT_N < 137.2345;

14. Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345. Truncate your answer to  decimal places.
-- Solution
SELECT ROUND(MAX(LAT_N), 4)
FROM STATION
WHERE LAT_N < 137.2345;

2. Query the following two values from the STATION table:

The sum of all values in LAT_N rounded to a scale of  decimal places.
The sum of all values in LONG_W rounded to a scale of  decimal places.
-- Solution
SELECT ROUND(SUM(LAT_N), 4), ROUND(SUM(LONG_W), 4)
FROM STATION;

15. Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than 137.2345. Round your answer to 4 decimal places
-- Solution
SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N = (SELECT MAX(LAT_N) FROM STATION WHERE LAT_N < 137.2345);

16. Query the smallest Northern Latitude (LAT_N) from STATION that is greater than 38.7880. Round your answer to 4 decimal places.
-- Solution
SELECT ROUND(MIN(LAT_N), 4)
FROM STATION
WHERE LAT_N > 38.7780;

17. Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than 38.7780. Round your answer to 4 decimal places.
-- Solution
SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N = (SELECT MIN(LAT_N) FROM STATION WHERE LAT_N > 38.7780);

18. Query the names of the country where the Northernmost Northern Latitude (LAT_N) meets the Westernmost Western Longitude (LONG_W) in the STATION table.
-- Solution
SELECT CITY
FROM STATION
WHERE LAT_N = (SELECT MAX(LAT_N) FROM STATION)
AND LONG_W = (SELECT MIN(LONG_W) FROM STATION);

19. Consider P1(a,b) and P2(c,d) to be two points on a 2D plane.
a happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
b happens to equal the minimum value in Western Longitude (LONG_W in STATION).
c happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
d happens to equal the maximum value in Western Longitude (LONG_W in STATION).
Query the Manhattan Distance between points P1 and P2 and round it to a scale of 4 decimal places.
-- Solution
SELECT ROUND(ABS(MAX(LAT_N) - MIN(LAT_N)) + ABS(MAX(LONG_W) - MIN(LONG_W)), 4)
FROM STATION;

20. Query the Euclidean Distance between points P1 and P2 and round it to a scale of 4 decimal places.
-- Solution
SELECT ROUND(SQRT(POW(MAX(LAT_N) - MIN(LAT_N), 2) + POW(MAX(LONG_W) - MIN(LONG_W), 2)), 4)
FROM STATION;

21. A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to 4 decimal places.
-- Solution
SELECT ROUND(LAT_N, 4)
FROM STATION
ORDER BY LAT_N
LIMIT 1 OFFSET (SELECT COUNT(LAT_N) / 2 FROM STATION);
