import numpy as np
import pandas as pd
from datetime import date, timedelta


def r22_26():
    """
        -- r22-26 --
        description:    Adults with most recent discharge facility (last 30 days) for Crisis Emergency Screenings
        author notes:
    """
    df = pd.read_csv('C:/Users/mingus/Documents/r22-26.csv')
    # drop all clients less than 18 y/o
    today = date.today().strftime('%Y-%m-%d')
    df["dob"] = pd.to_datetime(df.dob)
    df['dob'] = df['dob'].apply(lambda dob: (pd.to_datetime(today) - dob) / np.timedelta64(1, 'Y'))
    df = df[df['dob'] >= 18]
    df = df[df['program_name'] == 'Crisis Screening Services']

    crisis_src = pd.read_excel('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx')
    curr_date = (date.today().replace(day=1) - timedelta(days=1)).strftime('%b_%Y').lower()

    # sort the hospitals into their appropriate row
    for answer in df['answers_caption']:
        if 'STCF' in answer:
            crisis_src.loc[20, curr_date] = crisis_src.loc[20, curr_date] + 1
        if 'Other Involuntary Facility' in answer:
            crisis_src.loc[21, curr_date] = crisis_src.loc[21, curr_date] + 1
        if 'County Hospital' in answer:
            crisis_src.loc[22, curr_date] = crisis_src.loc[22, curr_date] + 1
        if 'State Hospital' in answer:
            crisis_src.loc[23, curr_date] = crisis_src.loc[23, curr_date] + 1
        if 'Voluntary Inpatient Facility' in answer:
            crisis_src.loc[24, curr_date] = crisis_src.loc[24, curr_date] + 1

    # sum each row
    for idx, row in crisis_src.loc[20:24, :].iterrows():
        crisis_src.loc[idx, 'SFY 2021 Total'] = row.iloc[4:16].sum()

    xl_writer = pd.ExcelWriter('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


r22_26()
