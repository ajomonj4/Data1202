import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

file_name = 'videogame/vg_sales.csv'

raw_df = pd.read_csv(file_name)

print(raw_df.head())

# how many games per platform
# unique_counts = raw_df.groupby('Platform')['Name'].nunique()


def num_games(_df):
    _games_df = _df.groupby('Platform')['Name'].count().reset_index()
    return _games_df

games_df = num_games(raw_df)

wb = Workbook()