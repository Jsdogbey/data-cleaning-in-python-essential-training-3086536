# %%
import pandas as pd
#sajfa
# %%
df = pd.read_csv('cart.csv', parse_dates=['date'])
df

#missing data analysis in python.

# %%
df['amount'].astype('Int32')

# %%
df.isnull()

# %%
df.isnull().any(axis=1)
