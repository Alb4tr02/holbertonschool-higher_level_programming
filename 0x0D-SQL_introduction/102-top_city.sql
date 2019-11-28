-- Order Group and Limit
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE temperatures.month = 7 OR temperatures.month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
