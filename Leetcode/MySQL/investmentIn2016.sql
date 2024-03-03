Table: Insurance

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| pid         | int   |
| tiv_2015    | float |
| tiv_2016    | float |
| lat         | float |
| lon         | float |
+-------------+-------+
pid is the primary key (column with unique values) for this table.
Each row of this table contains information about one policy where:
pid is the policyholders policy ID.
tiv_2015 is the total investment value in 2015 and tiv_2016 is the total investment value in 2016.
lat is the latitude of the policy holder's city. It's guaranteed that lat is not NULL.
lon is the longitude of the policy holder's city. It's guaranteed that lon is not NULL.

Write a solution to report the sum of all total investment values in 2016 tiv_2016, for all policyholders who:

have the same tiv_2015 value as one or more other policyholders, and
are not located in the same city as any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).
Round tiv_2016 to two decimal places.

Example

Insurance table:
+------------+----------+----------+-------+--------+
| pid        | tiv_2015 | tiv_2016 | lat   | lon    |
+------------+----------+----------+-------+--------+
| 1          | 10       | 5        | 10.0  | 10.0   |
| 2          | 20       | 20       | 20.0  | 20.0   |
| 3          | 10       | 30       | 20.0  | 20.0   |
| 4          | 10       | 40       | 40.0  | 40.0   |
| 5          | 50       | 50       | 50.0  | 50.0   |
+------------+----------+----------+-------+--------+

-- Write your MySQL query statement below

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM insurance
WHERE tiv_2015 IN
(
    SELECT tiv_2015 
    FROM insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
) AND CONCAT(lat, lon) IN
(
    SELECT CONCAT(lat, lon) 
    FROM insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
);
