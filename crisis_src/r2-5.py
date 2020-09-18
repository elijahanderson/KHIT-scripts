import numpy as np
import pandas as pd
from datetime import date, datetime


def main():
    """
        -- r49-73 --
        description:    Final script that fills out rows 2-5 and inserts formula calculations.
        author notes:
    """
    df = pd.read_csv('C:/Users/mingus/Documents/r2-5.csv')
    df['dob'] = pd.to_datetime(df.dob)

    crisis_src = pd.read_excel('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx')
    curr_date_col = date.today().strftime('%b_%Y').lower()
    time_format = '%Y-%m-%d'
    curr_date = date.today().strftime(time_format)

    # for every client, increment the appropriate row based on their age (>=18 and <18) as well as the total row
    by_client = df.groupby('full_name')
    for client, frame in by_client:
        frame = frame.reset_index(drop=True)
        year_diff = (pd.to_datetime(curr_date) - frame.loc[0, 'dob']) / np.timedelta64(1, 'Y')
        if year_diff >= 18:
            crisis_src.loc[1, curr_date_col] = crisis_src.loc[1, curr_date_col] + 1
        else:
            crisis_src.loc[2, curr_date_col] = crisis_src.loc[2, curr_date_col] + 1
        crisis_src.loc[3, curr_date_col] = crisis_src.loc[3, curr_date_col] + 1

    # sum each row
    for idx, row in crisis_src.loc[0:3, :].iterrows():
        crisis_src.loc[idx, 'SFY 2021 Total'] = row.iloc[4:16].sum()

    xl_writer = pd.ExcelWriter('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


main()
