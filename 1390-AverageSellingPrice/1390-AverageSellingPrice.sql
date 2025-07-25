-- Last updated: 7/15/2025, 6:26:43 PM
SELECT 
    p.product_id,
    IF(IFNULL(SUM(u.units), 0) = 0, 0, ROUND(SUM(u.units * p.price) / SUM(u.units), 2)) AS average_price
FROM 
    Prices p
LEFT JOIN 
    UnitsSold u
    ON p.product_id = u.product_id
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY 
    p.product_id;
