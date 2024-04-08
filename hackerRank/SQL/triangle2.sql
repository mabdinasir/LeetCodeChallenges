P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

* 
* * 
* * * 
* * * * 
* * * * *
Write a query to print the pattern P(20).

-- Solution
set @num := 0;

SELECT REPEAT('* ', @num := @num +1)
FROM information_schema.TABLES
WHERE @num < 20;