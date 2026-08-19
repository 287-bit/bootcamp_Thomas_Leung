import pandas as pd

def get_min(df):
    for col in df:
        if pd.api.types.is_numeric_dtype(df[col]):
            print(col)
            print(df[col].min())
