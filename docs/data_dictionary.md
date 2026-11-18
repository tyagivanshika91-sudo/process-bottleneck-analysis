
# Data Dictionary – Order-to-Delivery Analysis

## Dataset Overview
The dataset contains 1,000 simulated e-commerce orders created for analyzing order processing and delivery performance.

## Column Descriptions

| Column | Description |
|---|---|
| order_id | Unique order identification number |
| order_date | Date and time when order was placed |
| region | Customer delivery region |
| order_value | Total order value |
| processing_hours | Time taken to process an order |
| packaging_hours | Time taken to package an order |
| shipping_hours | Time spent in shipping |
| delivery_hours | Time spent in final delivery |
| total_delivery_hours | Total time across all process stages |
| delivery_status | Whether the order was Late or On Time |

## Process Stages

1. Processing – Preparing and confirming the order.
2. Packaging – Packing the ordered products.
3. Shipping – Transportation and shipment movement.
4. Delivery – Final delivery to the customer.

## Derived Metrics

- Total Delivery Time = Processing + Packaging + Shipping + Delivery
- Late Delivery Percentage = (Late Orders / Total Orders) × 100
- Average Stage Time = Total Time in a Stage / Number of Orders

## Data Generation
- Total records: 1,000
- Data type: Synthetic / Simulated
- Random seed: 42
- Dataset generated using Python, Pandas and NumPy.

## Important Note
This dataset is created for educational and portfolio purposes. It does not represent real customer transactions or actual business operations.
