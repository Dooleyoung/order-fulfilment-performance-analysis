import pandas as pd

# Load raw data
df = pd.read_csv('../data/raw_sales_data.csv', parse_dates=['order_date'])

# Clean data
df['sales_amount'] = pd.to_numeric(df['sales_amount'], errors='coerce')

# Generate summary report
summary = df.groupby('region')['sales_amount'].agg(
    total_sales='sum',
    average_sales='mean'
).reset_index()

# Save output
summary.to_csv('../output/summary_report.csv', index=False)

print("Automated report generated successfully.")
