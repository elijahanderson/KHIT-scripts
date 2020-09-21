import numpy as np
import pandas as pd
from datetime import date, datetime


def r28_29():
    """
        -- r18-20 --
        description:    Adults with a Crisis Triage event and Outreach event within 1-2 or > 2 hours of each other
        author notes:
    """
    df = pd.read_csv('C:/Users/mingus/Documents/r28-29.csv')
    # drop all clients less than 18 y/o
    today = date.today().strftime('%Y-%m-%d')
    df["dob"] = pd.to_datetime(df.dob)
    df['dob'] = df['dob'].apply(lambda dob: (pd.to_datetime(today) - dob) / np.timedelta64(1, 'Y'))
    df = df[df['dob'] > 18]
    df.sort_values(by=['full_name', 'actual_date'], inplace=True)
    df = df.reset_index(drop=True)
    # convert to pd datetime for date operations
    df["actual_date"] = pd.to_datetime(df.actual_date)
    # rename for legibility
    df = df.rename(columns={'actual_date': 'date', 'actual_date.1': 'time'})

    outreaches = pd.read_csv('C:/Users/mingus/Documents/r6-14.csv')
    outreaches['actual_date'] = pd.to_datetime(outreaches.actual_date)
    outreaches = outreaches.rename(columns={'actual_date': 'outreach_date'})
    outreaches['full_name'] = outreaches['last_name'] + ', ' + outreaches['first_name']
    outreaches = outreaches[['full_name', 'outreach_date']]

    df = df.merge(outreaches, on='full_name')

    by_client = df.groupby('full_name')
    curr_date = date.today().strftime('%b_%Y').lower()
    crisis_src = pd.read_excel('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx')
    time_format = '%I:%M %p'

    # for each client
    for client, frame in by_client:
        frame = frame.reset_index(drop=True)
        for idx, row in frame.iterrows():
            # increment the appropriate row according to the time difference (1-2 or >=2 hours)
            if str(row['date'])[0:10] == str(frame.loc[idx, 'outreach_date'])[0:10]:
                tdelta = datetime.strptime(str(frame.loc[idx, 'outreach_date'])[11:], '%H:%M:%S') - \
                         datetime.strptime(row['time'], time_format)
                hr_diff = tdelta.seconds / 3600
                # between 1 & 2 hours
                if 1.0 <= hr_diff < 2.0:
                    crisis_src.loc[26, curr_date] = crisis_src.loc[26, curr_date] + 1
                # over 2 hours
                elif hr_diff >= 2.0:
                    crisis_src.loc[27, curr_date] = crisis_src.loc[27, curr_date] + 1

    # sum each program
    for idx, row in crisis_src.loc[26:27, :].iterrows():
        crisis_src.loc[idx, 'SFY 2021 Total'] = row.iloc[4:16].sum()

    xl_writer = pd.ExcelWriter('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


r28_29()
