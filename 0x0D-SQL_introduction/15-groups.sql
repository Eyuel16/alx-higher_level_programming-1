-- lists the score and repeatition of the score in descending order
SELECT score, COUNT(score) AS 'number' FROM second_table GROUP BY score ORDER BY number DESC;
