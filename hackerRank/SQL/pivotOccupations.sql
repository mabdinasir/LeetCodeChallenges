-- Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. The output column headers should be Doctor, Professor, Singer, and Actor, respectively.

-- Note: Print NULL when there are no more names corresponding to an occupation.

-- Solution
select
Max(if(occupation='Doctor',name,null)) Doctor,
Max(if(occupation='Professor',name,null)) Professor,
Max(if(occupation='Singer',name,null)) Singer,
Max(if(occupation='Actor',name,null)) Actor
FROM (select name, occupation, row_number() over (partition by occupation order by name) as row_n from occupations) as x
group by x.row_n;