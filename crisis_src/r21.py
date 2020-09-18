import numpy as np
import pandas as pd
from datetime import date, datetime


def r21():
    """
        -- r21 --
        description:    Adults who have been discharged and readmitted to Crisis in fewer than 30 days.
        author notes:   Enrollment end dates include the previous as well as the current month due to the report
                        requirements.
    """
    df = pd.read_csv('C:/Users/mingus/Documents/r21.csv')
    df = df.dropna(subset=['end_date'], axis=0)
    df["actual_date"] = pd.to_datetime(df.actual_date)
    df["end_date"] = pd.to_datetime(df.end_date)
    # drop all clients less than 18 y/o
    today = date.today().strftime('%Y-%m-%d')
    df["dob"] = pd.to_datetime(df.dob)
    df['dob'] = df['dob'].apply(lambda dob: (pd.to_datetime(today) - dob) / np.timedelta64(1, 'Y'))
    df = df[df['dob'] > 18]
    df.sort_values(by=['full_name', 'actual_date'], inplace=True)
    # Drop unique rows -- target clients will have more than one enrollment event
    df = df[df.duplicated(subset=['full_name'], keep=False)]
    df = df.reset_index()
    # convert to datetime for date operations
    df["actual_date"] = pd.to_datetime(df.actual_date)
    df["end_date"] = pd.to_datetime(df.end_date)
    # rename for legibility
    df = df.rename(columns={'actual_date.1': 'start_time', 'end_date.1': 'end_time'})

    by_client = df.groupby('full_name')
    curr_date = date.today().strftime('%b_%Y').lower()
    time_format = '%Y-%m-%d %I:%M %p'
    crisis_src = pd.read_excel('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx')

    # for each client
    for client, frame in by_client:
        # get the 2 most recent enrollments
        frame = frame.tail(2)
        frame = frame.reset_index()

        start_date = str(frame.loc[1, 'actual_date'])[0:10] + ' ' + str(frame.loc[1, 'start_time'])
        end_date = str(frame.loc[0, 'end_date'])[0:10] + ' ' + str(frame.loc[0, 'end_time'])
        print(start_date, end_date)
        tdelta = datetime.strptime(end_date, time_format) - datetime.strptime(start_date, time_format)
        # if there were fewer than 30 days between the 2, increment row 21 of the megareport
        if tdelta.days < 30:
            crisis_src.loc[19, curr_date] = crisis_src.loc[19, curr_date] + 1

    # sum the row
    crisis_src.loc[19, 'SFY 2021 Total'] = crisis_src.iloc[19, 4:16].sum()

    xl_writer = pd.ExcelWriter('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


r21()
