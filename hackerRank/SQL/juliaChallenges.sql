Julia asked her students to create some coding challenges. Write a query to print the hacker_id, name, and the total number of challenges created by each student. 
Sort your results by the total number of challenges in descending order. 
If more than one student created the same number of challenges, then sort the result by hacker_id. 
If more than one student created the same number of challenges and the count is less than the maximum number of challenges created, 
then exclude those students from the result.

Input Format

The following tables contain challenge data:

Hackers: The hacker_id is the id of the hacker, and name is the name of the hacker. 

Challenges: The challenge_id is the id of the challenge, and hacker_id is the id of the student who created the challenge. 

Sample Input 0

Hackers Table:  Challenges Table: 

Sample Output 0

21283 Angela 6
88255 Patrick 5
96196 Lisa 1
Sample Input 1

Hackers Table:  Challenges Table: 

Sample Output 1

12299 Rose 6
34856 Angela 6
79345 Frank 4
80491 Patrick 3
81041 Lisa 1
Explanation

For Sample Case 0, we can get the following details:

Students  and  both created  challenges, but the maximum number of challenges created is  so these students are excluded from the result.

For Sample Case 1, we can get the following details:

Students  and  both created  challenges. Because  is the maximum number of challenges created, these students are included in the result.

1
​
Line: 1 Col: 1
Run Code Submit CodeUpload Code as File
BlogScoringEnvironmentFAQAbout UsSupportCareersTerms Of ServicePrivacy Policy

-- Solution :
WITH CTE_B AS (
    SELECT C.Hacker_id, H.Name, COUNT(C.Challenge_id) AS Challenges_Count, 
    RANK() OVER (ORDER BY COUNT(C.Challenge_id) DESC) AS Ranks, 
    DENSE_RANK() OVER (ORDER BY COUNT(C.Challenge_id) DESC) AS Dense_Ranks 
    FROM Hackers H 
    JOIN Challenges C ON H.Hacker_id = C.Hacker_id 
    GROUP BY C.Hacker_id, H.Name 
), 
CTE_D AS (
    SELECT Challenges_Count, Ranks, COUNT(Dense_Ranks) AS Dense_Ranks_Count 
    FROM CTE_B 
    GROUP BY Challenges_Count, Ranks 
    HAVING Ranks = 1 OR (Ranks > 1 AND COUNT(Dense_Ranks) = 1) 
    ORDER BY Ranks 
) 
SELECT CTE_B.Hacker_id, CTE_B.Name, CTE_D.Challenges_count 
FROM CTE_D 
JOIN CTE_B ON CTE_B.Challenges_count = CTE_D.Challenges_count 
ORDER BY CTE_D.Challenges_count DESC, CTE_B.Hacker_id;
