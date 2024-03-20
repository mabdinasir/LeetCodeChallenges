-- Union of Set A and Set B:
-- explanation: This is the set of all elements in Set A and Set B.
SELECT * FROM A UNION SELECT * FROM B;

-- Intersection of Set A and Set B:
-- explanation: This is the set of elements that are in both Set A and Set B.
SELECT * FROM A INTERSECT SELECT * FROM B;

Set A subtract Set B:
-- explanation: This is the set of elements that are only in Set A.
SELECT * FROM A WHERE NOT EXISTS (SELECT * FROM B WHERE A.element = B.element);

Set B subtract Set A:
-- explanation: This is the set of elements that are only in Set B.
SELECT * FROM B WHERE NOT EXISTS (SELECT * FROM A WHERE B.element = A.element);

-- Union of Set A and Set B, excluding common elements:
-- explanation: This is the set of all elements in Set A and Set B, excluding the elements that are in both Set A and Set B.
SELECT * FROM A
UNION
SELECT * FROM B
WHERE NOT EXISTS (SELECT * FROM A WHERE B.element = A.element);

-- Set A subtracted from the union of Set A and Set B:
-- explanation: This is the set of elements that are only in Set A.
SELECT * FROM A WHERE NOT EXISTS (SELECT * FROM B WHERE A.element = B.element);

-- Set B subtracted from the union of Set A and Set B:
-- explanation: This is the set of elements that are only in Set B.
SELECT * FROM B WHERE NOT EXISTS (SELECT * FROM A WHERE B.element = A.element);

-- Symmetric difference of Set A and Set B:
-- explanation: This is the set of elements that are in Set A and Set B but not in both.
(SELECT * FROM A WHERE NOT EXISTS (SELECT * FROM B WHERE A.element = B.element))
UNION
(SELECT * FROM B WHERE NOT EXISTS (SELECT * FROM A WHERE B.element = A.element));

-- You are given two sets.
-- Set A = {1,2,3,4,5,6}
-- Set B = {2,3,4,5,6,7,8}
-- What is the total number of ordered pairs present in the Cartesian Product  ? Only enter the correct integer in the answering box. Do not include any extra spaces, tabs or newlines.
-- A X B:
-- explanation: This is the set of all possible ordered pairs (a, b) where a is in Set A and b is in Set B.
SELECT * FROM A, B;
-- Total number of ordered pairs = 6 * 7 = 42



--1. Consider the following data table named Student.
Student Name    Number  Sex  
Ben             3412    M  
Dan             1234    M  
Nel             2341    F  

-- What is the count of rows returned in the following relational selection?
σ(Number<3000)(Student)
-- Only the row where Number is less than 3000 will be selected. Hence, only 2 rows will be returned.


--2. Consider the following data table named Student.
Name                Number  Sex  
Nina                3412    F 
Mike                1234    M  
Nelson              2341    F  

-- What is the count of attributes (columns) returned in the following projection?
-- π(Name, Number)(Student)

-- Only the Name and Number columns will be returned. Hence, 2 attributes will be returned.

-- 3. Consider the following data table named Student.
Student Name        Number  Sex  
Nina                3412    F 
Mike                1234    M  
Nelson              2341    F  

-- Here is another data table named Teaching Assistants
Subject     ID
Physics     3412
Chemistry   1111
Mathematics 2341  

-- What is the count of rows returned in the following join operation?
Student ⊳⊲(Number=ID) Teaching Assistants
-- Only the rows where Number is equal to ID will be returned. Hence, only 2 rows will be returned.

-- 4. which is a join condition that contains an inequality operator?
-- A join condition that contains an inequality operator is a non-equijoin. A non-equijoin is a join condition that contains an inequality operator such as <, >, <=, >=, or <>. For example, the join condition A.x < B.y is a non-equijoin.

-- 5. Consider the following data table named Student.