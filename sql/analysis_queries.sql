
-- 1. Average time spent at each process stage
SELECT
    AVG(processing_hours) AS avg_processing_hours,
    AVG(packaging_hours) AS avg_packaging_hours,
    AVG(shipping_hours) AS avg_shipping_hours,
    AVG(delivery_hours) AS avg_delivery_hours
FROM orders;


-- 2. Late delivery percentage
SELECT
    COUNT(*) AS total_orders,
    SUM(CASE WHEN delivery_status = 'Late' THEN 1 ELSE 0 END) AS late_orders,
    ROUND(
        100.0 * SUM(CASE WHEN delivery_status = 'Late' THEN 1 ELSE 0 END)
        / COUNT(*), 2
    ) AS late_delivery_percentage
FROM orders;


-- 3. Region-wise delivery performance
SELECT
    region,
    COUNT(*) AS total_orders,
    ROUND(AVG(total_delivery_hours), 2) AS avg_delivery_hours,
    SUM(CASE WHEN delivery_status = 'Late' THEN 1 ELSE 0 END) AS late_orders
FROM orders
GROUP BY region
ORDER BY late_orders DESC;


-- 4. Identify the main bottleneck
SELECT
    'Processing' AS process_stage,
    ROUND(AVG(processing_hours), 2) AS avg_hours
FROM orders

UNION ALL

SELECT
    'Packaging',
    ROUND(AVG(packaging_hours), 2)
FROM orders

UNION ALL

SELECT
    'Shipping',
    ROUND(AVG(shipping_hours), 2)
FROM orders

UNION ALL

SELECT
    'Delivery',
    ROUND(AVG(delivery_hours), 2)
FROM orders;
