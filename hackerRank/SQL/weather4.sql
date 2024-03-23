Find the difference between the total number of CITY entries in the table and the 
number of DISTINCT CITY entries in the table.

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
SELECT COUNT(city) - COUNT(DISTINCT city) FROM station;
