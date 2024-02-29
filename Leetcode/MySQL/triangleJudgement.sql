Table: Triangle

+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.

Report for every three line segments whether they can form a triangle.

Return the result table in any order.

The result format is in the following example.


Example 1:

Input: 
Triangle table:
+----+----+----+
| x  | y  | z  |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+
Output: 
+----+----+----+----------+
| x  | y  | z  | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
+----+----+----+----------+

Create table If Not Exists Triangle (x int, y int, z int)
Truncate table Triangle
insert into Triangle (x, y, z) values ('13', '15', '30')
insert into Triangle (x, y, z) values ('10', '20', '15')

-- how to run this file in terminal
-- mysql -u root -p < triangleJudgement.sql

SELECT x, y, z, 
    CASE 
        WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
        ELSE 'No'
    END AS triangle

-- solution 2
SELECT x, y, z, 
    IF(x + y > z AND x + z > y AND y + z > x, 'Yes', 'No') AS triangle


-- solution 3
select *, if(x + y > z and x + z > y and y + z > x, 'Yes', 'No') as triangle from triangle
