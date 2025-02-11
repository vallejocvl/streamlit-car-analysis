import pandas as pd

def data_cleaner(df: pd.DataFrame):
    df = df.dropna(subset=["Brand"])
    