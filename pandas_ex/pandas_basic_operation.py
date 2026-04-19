import pandas as pd
from pathlib import Path
_dir_ = Path(__file__).parent
_end = '\n\n'
#df  = pd.read_csv(_dir_/'dataset'/'career.csv')
df = pd.read_csv(_dir_.joinpath('dataset/career.csv'))

print('#-----# access one col',end=_end)
print(df['Preferred_Career_2026'],end=_end)

print('#-----# access multiple cols',end=_end)
print(df[['Preferred_Career_2026','Age']],end=_end)

print('#-----#  slicing - exist 2 ways (loc & iloc)',end=_end)
print(df.loc[0:5,['Preferred_Career_2026','Age']],end=_end)
print(df.iloc[0:5,[2,5]],end=_end)