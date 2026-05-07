# Data
We are using US Treasury Yields Data.
The data used in this project is **not included** in this repository.

## Source

US Treasury constant maturity yields are freely available from the 
Federal Reserve Bank of St. Louis (FRED):

https://fred.stlouisfed.org

## How to Download

1. Go to the FRED website linked above
2. Search for the following series codes and download each as CSV:

| Series Code | Maturity |
|-------------|----------|
| DGS1MO      | 1-month  |
| DGS3MO      | 3-month  |
| DGS6MO      | 6-month  |
| DGS1        | 1-year   |
| DGS2        | 2-year   |
| DGS3        | 3-year   |
| DGS5        | 5-year   |
| DGS7        | 7-year   |
| DGS10       | 10-year  |
| DGS20       | 20-year  |
| DGS30       | 30-year  |

## Alternative — Download All at Once

If you have a FRED API key, the notebook can download all series 
automatically. Get a free API key at:

https://fred.stlouisfed.org/docs/api/api_key.html

Then set your key at the top of the notebook:
```python
FRED_API_KEY = "your_key_here"
```

## Date Used in This Project

The analysis uses a snapshot of US Treasury yields on **2024-09-13**.
