You are given a table, Functions, containing two columns: X and Y.



Two pairs (X1, Y1) and (X2, Y2) are said to be symmetric pairs if X1 = Y2 and X2 = Y1.

Write a query to output all such symmetric pairs in ascending order by the value of X. List the rows such that X1 ≤ Y1.

-- Solution
SELECT a.X, a.Y
FROM Functions AS a
CROSS JOIN Functions AS b
WHERE a.X = b.Y AND b.X = a.Y AND a.X != a.Y AND a.X < a.Y
UNION
SELECT X, Y
FROM Functions
GROUP BY X, Y
HAVING COUNT(*) > 1
ORDER BY X ASC
