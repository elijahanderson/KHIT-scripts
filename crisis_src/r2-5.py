import numpy as np
import pandas as pd
from datetime import date, timedelta


def main():
    """
        -- r49-73 --
        description:    Final script that fills out rows 2-5 and inserts formula calculations.
        author notes:   Not sure to count all admissions or just unique clients?
    """
    df = pd.read_csv('C:/Users/mingus/Documents/r2-5.csv')
    today = date.today().strftime('%Y-%m-%d')
    df = df.rename(columns={'Date of Birth': 'dob'})
    df['dob'] = pd.to_datetime(df.dob)
    df['dob'] = df['dob'].apply(lambda dob: (pd.to_datetime(today) - dob) / np.timedelta64(1, 'Y'))
    adults = df[df['dob'] >= 18]
    minors = df[df['dob'] < 18]

    crisis_src = pd.read_excel('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx')
    curr_date = (date.today().replace(day=1) - timedelta(days=1)).strftime('%b_%Y').lower()

    crisis_src.loc[1, curr_date] = len(adults)
    crisis_src.loc[2, curr_date] = len(minors)
    crisis_src.loc[3, curr_date] = len(df)

    # sum each row
    for idx, row in crisis_src.loc[0:3, :].iterrows():
        crisis_src.loc[idx, 'SFY 2021 Total'] = row.iloc[4:16].sum()

    xl_writer = pd.ExcelWriter('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


main()
