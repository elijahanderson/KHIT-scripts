import numpy as np
import pandas as pd
from datetime import date


def r6_14():
    """
        -- r6-14 --
        description:    Adults admitted to Crisis and served by Mobile Outreach in various locations
        author notes:
    """
    df = pd.read_csv('C:/Users/mingus/Documents/r6-14.csv')
    # drop all clients less than 18 y/o
    today = date.today().strftime('%Y-%m-%d')
    df["dob"] = pd.to_datetime(df.dob)
    df['dob'] = df['dob'].apply(lambda dob: (pd.to_datetime(today) - dob) / np.timedelta64(1, 'Y'))
    df = df[df['dob'] > 18]

    crisis_src = pd.read_excel('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx')
    curr_date = date.today().strftime('%b_%Y').lower()

    # sort the resulting outreaches into their appropriate row
    by_client = df.groupby('full_name')
    clients_checked = []
    for client, frame in by_client:
        for answer in frame['answers_caption']:
            if 'Correctional' in answer:
                if client not in clients_checked:
                    crisis_src.loc[13, curr_date] = crisis_src.loc[13, curr_date] + 1
                crisis_src.loc[4, curr_date] = crisis_src.loc[4, curr_date] + 1
            if 'Nursing' in answer:
                if client not in clients_checked:
                    crisis_src.loc[13, curr_date] = crisis_src.loc[13, curr_date] + 1
                crisis_src.loc[5, curr_date] = crisis_src.loc[5, curr_date] + 1
            elif 'ER' in answer:
                crisis_src.loc[6, curr_date] = crisis_src.loc[6, curr_date] + 1
            elif 'Inpatient' in answer:
                if client not in clients_checked:
                    crisis_src.loc[13, curr_date] = crisis_src.loc[13, curr_date] + 1
                crisis_src.loc[7, curr_date] = crisis_src.loc[7, curr_date] + 1
            elif 'Med Unit' in answer:
                if client not in clients_checked:
                    crisis_src.loc[13, curr_date] = crisis_src.loc[13, curr_date] + 1
                crisis_src.loc[8, curr_date] = crisis_src.loc[8, curr_date] + 1
            elif 'Community' in answer:
                if client not in clients_checked:
                    crisis_src.loc[13, curr_date] = crisis_src.loc[13, curr_date] + 1
                crisis_src.loc[11, curr_date] = crisis_src.loc[11, curr_date] + 1
        clients_checked.append(client)

    # sum the column
    crisis_src.loc[12, curr_date] = crisis_src.loc[4:11, curr_date].sum()

    # sum each row
    for idx, row in crisis_src.loc[4:12, :].iterrows():
        crisis_src.loc[idx, 'SFY 2021 Total'] = row.iloc[4:16].sum()

    xl_writer = pd.ExcelWriter('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


r6_14()