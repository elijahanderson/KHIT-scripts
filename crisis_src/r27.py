import numpy as np
import pandas as pd
from datetime import date


def r27():
    """
        -- r27 --
        description:    Number of transfers with Crisis stay length >= 24 hours
        author notes:   The date diff is calculated in the custom report itself on this one.
    """
    df = pd.read_csv('C:/Users/mingus/Documents/r27.csv')
    # drop all clients less than 18 y/o
    today = date.today().strftime('%Y-%m-%d')
    df["dob"] = pd.to_datetime(df.dob)
    df['dob'] = df['dob'].apply(lambda dob: (pd.to_datetime(today) - dob) / np.timedelta64(1, 'Y'))
    df = df[df['dob'] > 18]
    curr_date = date.today().strftime('%b_%Y').lower()
    crisis_src = pd.read_excel('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx')
    # set row 27 to the length of the dataframe
    crisis_src.loc[25, curr_date] = len(df)

    # sum the row
    crisis_src.loc[25, 'SFY 2021 Total'] = crisis_src.iloc[25, 4:16].sum()

    xl_writer = pd.ExcelWriter('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


r27()
