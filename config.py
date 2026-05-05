OBSERVATION_START="1975-01-01"
OBSERVATION_END="2026-02-01"
VALUATION_DATE = "2024-09-14"

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
VAR_CONFIDENCE  = [0.95, 0.99]
LOOKBACK_DAYS   = 252