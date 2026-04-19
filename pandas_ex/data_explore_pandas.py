import pandas as pd
from pathlib import Path
_dir_ = Path(__file__).parent

#df  = pd.read_csv(_dir_/'dataset'/'career.csv')
df = pd.read_csv(_dir_.joinpath('dataset/career.csv'))

#show 5 first record
print(df.head())

#show 5 last record
print(df.tail())
