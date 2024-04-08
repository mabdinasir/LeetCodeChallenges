You did such a great job helping Julia with her last coding contest challenge that she wants you to work on this one, too!

The total score of a hacker is the sum of their maximum scores for all of the challenges. Write a query to print the hacker_id, name, and total score of the hackers ordered by the descending score. If more than one hacker achieved the same total score, then sort the result by ascending hacker_id. Exclude all hackers with a total score of  from your result.

Input Format

The following tables contain contest data:

Hackers: The hacker_id is the id of the hacker, and name is the name of the hacker.

-- Solution

SELECT h.hacker_id, h.name, SUM(sub_score.score) AS total_score 
FROM hackers AS h 
INNER JOIN ( 
    SELECT hacker_id, MAX(score) AS score 
    FROM submissions 
    GROUP BY challenge_id, hacker_id 
) AS sub_score ON h.hacker_id = sub_score.hacker_id 
GROUP BY h.hacker_id, h.name 
HAVING SUM(sub_score.score) > 0 
ORDER BY total_score DESC, h.hacker_id;
