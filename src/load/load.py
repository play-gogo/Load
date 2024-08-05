from transform.transform import transform
import pandas as pd


def load(load_dt='20200101'):
    df = transform(load_dt)
    df = df.to_parquet("~/tmp/load", partition_cols=['load_dt'])
    
    print(df)
    return df

load()