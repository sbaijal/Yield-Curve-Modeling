import numpy as np
import pandas as pd
from fredapi import Fred
from config import FRED_API_KEY, OBSERVATION_END, OBSERVATION_START, SERIES_IDS

fred = Fred(api_key=FRED_API_KEY)

def get_yield_data(series_id):
    data = fred.get_series(series_id, observation_start=OBSERVATION_START, observation_end=OBSERVATION_END)
    return data

def load_fred_data():
    yields_dict = {series_id : get_yield_data(series_id) for series_id in SERIES_IDS}
    yields = pd.DataFrame(yields_dict)

    yields.columns = ['1 Month', '3 Month', '6 Month', '1 Year', '2 Year', '3 Year', '5 Year', '7 Year', '10 Year', '20 Year', '30 Year']
    return yields