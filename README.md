
# Process Bottleneck Analysis – Order-to-Delivery

## Project Overview
This project analyzes a simulated e-commerce order-to-delivery process to identify bottlenecks and understand the factors contributing to late deliveries.

The analysis covers four stages:
- Order Processing
- Packaging
- Shipping
- Final Delivery

## Business Objectives
- Identify the most time-consuming process stage.
- Calculate the percentage of late deliveries.
- Compare delivery performance across regions.
- Provide data-driven recommendations for process improvement.

## Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- SQL

## Dataset
This project uses a simulated dataset of 1,000 e-commerce orders.

Each record contains:
- Order ID and order date
- Region and order value
- Processing time
- Packaging time
- Shipping time
- Delivery time
- Total delivery time
- Delivery status

**Note:** This is synthetic sample data created for portfolio and learning purposes. It does not represent actual company records.

## Key Findings

- Total orders analyzed: 1,000
- Late deliveries: 209
- Late delivery percentage: 20.9%
- Main bottleneck: Shipping stage
- Average shipping time: 27.91 hours
- Average delivery time: 14.09 hours
- East region had the highest late delivery percentage at 23.67%.

## Business Recommendations

1. Review shipping partner performance and transportation delays.
2. Monitor dispatch scheduling and shipment handover times.
3. Investigate the higher late delivery percentage in the East region.
4. Track stage-wise processing time regularly.
5. Set performance targets for each process stage.

## Project Structure

```text
process-bottleneck-analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   └── data_dictionary.md
│
├── outputs/
│
├── sql/
│   └── analysis_queries.sql
│
├── src/
│   ├── __init__.py
│   ├── generate_data.py
│   └── analyze_process.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate the sample dataset:

```bash
py src/generate_data.py
```

Run the analysis:

```bash
py src/analyze_process.py
```

Generated reports and charts are saved in the `outputs` folder.

## Limitations
- Dataset is simulated, not collected from a real business.
- Results depend on the assumptions used to generate sample data.
- Findings should not be interpreted as actual industry performance.

## Author
Vanshika Tyagi

Aspiring Business Analyst | Data Analyst
