import numpy as np
import pandas as pd
from datetime import date, timedelta


def r17():
    """
        -- r17 --
        description:    Adults discharged to the community after Crisis enrollment for greater than 4 and less than 24
                        hours.
        author notes:   Uses pre-defined Oaks SQL, so only need to count rows.
    """
    df = pd.read_csv('C:/Users/mingus/Documents/r17.csv')
    # drop all clients less than 18 y/o
    today = date.today().strftime('%Y-%m-%d')
    df = df.rename(columns={'Date of Birth': 'dob'})
    df['dob'] = pd.to_datetime(df.dob)
    df['dob'] = df['dob'].apply(lambda dob: (pd.to_datetime(today) - dob) / np.timedelta64(1, 'Y'))
    df = df[df['dob'] > 18]

    curr_date = (date.today().replace(day=1) - timedelta(days=1)).strftime('%b_%Y').lower()
    crisis_src = pd.read_excel('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx')
    # set row 17 to the length of the df
    crisis_src.loc[15, curr_date] = len(df)
    # sum the row
    crisis_src.loc[15, 'SFY 2021 Total'] = crisis_src.iloc[15, 4:16].sum()

    xl_writer = pd.ExcelWriter('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


r17()
