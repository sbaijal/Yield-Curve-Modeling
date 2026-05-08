'''
Config.py contains all the configuration parameters for the yield curve modeling and risk management project. This includes:
- Observation and valuation dates for the bond yield data.
- The series IDs for the US Treasury yields from FRED.
- The portfolio of bonds being analyzed, with their names, coupons, maturities, and face values.
- The FRED API key for data retrieval.
- Parameters for the stress testing, including parallel shock magnitudes.
- An array of maturities corresponding to the bond yields being analyzed.
'''

import numpy as np
OBSERVATION_START = "1975-01-01"
OBSERVATION_END = "2026-02-01"
VALUATION_DATE = "2024-09-13"

SERIES_IDS = ['DGS1MO', 'DGS3MO', 'DGS6MO', 'DGS1', 'DGS2', 'DGS3', 'DGS5', 'DGS7', 'DGS10', 'DGS20', 'DGS30']

PORTFOLIO = [
     #name               coupon     maturity year  face value(£m)
    ("UST 4.750% 2026",  4.750,         2.0,          50),
    ("UST 3.875% 2029",  3.875,         5.0,          120),
    ("UST 3.875% 2034",  3.875,         10.0,         90),
    ("UST 4.250% 2054",  4.250,         30.0,         40),
]

FRED_API_KEY = "3a4a21640f653124f86acdea283a9768"

# Stress test parameters
PARALLEL_SHOCKS = [-300, -200, -100, +100, +200, +300]

maturities = np.array([0.083, 0.25, 0.5, 1.0, 2.0, 3.0, 5.0, 7.0, 10.0, 20.0, 30.0])