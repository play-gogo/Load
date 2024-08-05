from transform.transform import transform
import pandas as pd


def load(load_dt='20200101'):
    df = transform(load_dt)
    df.to_parquet("~/code/playgogo/storage", partition_cols=['month','load_dt'])
    
load()
