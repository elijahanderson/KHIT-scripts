import numpy as np
import pandas as pd
from datetime import date, datetime


def r17():
    """
        -- r17 --
        description:    Adults discharged to the community after Crisis enrollment for greater than 4 and less than 24
                        hours.
        author notes:   May need to filter report to show only discharges to community in the future, but I think that
                        all discharges are to the community.
    """
    df = pd.read_csv('C:/Users/mingus/Documents/r17.csv')
    # drop all clients less than 18 y/o
    today = date.today().strftime('%Y-%m-%d')
    df["dob"] = pd.to_datetime(df.dob)
    df['dob'] = df['dob'].apply(lambda dob: (pd.to_datetime(today) - dob) / np.timedelta64(1, 'Y'))
    df = df[df['dob'] > 18]
    # sorting required for working algorithm
    df.sort_values(by=['full_name', 'actual_date'], inplace=True)
    df = df.reset_index(drop=True)

    # convert to datetime for date operations
    df["actual_date"] = pd.to_datetime(df.actual_date)
    df["end_date"] = pd.to_datetime(df.end_date)
    # rename for legibility
    df = df.rename(columns={'actual_date.1': 'start_time', 'end_date.1': 'end_time'})

    curr_date = date.today().strftime('%b_%Y').lower()
    crisis_src = pd.read_excel('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx')
    time_format = '%Y-%m-%d %I:%M %p'

    # if the time between actual_date and end_date is >= 4 or <= 24 hours, increment row 17 of the megareport
    for idx, row in df.iterrows():
        start_date = str(row['actual_date'])[0:10] + ' ' + str(row['start_time'])
        end_date = str(row['end_date'])[0:10] + ' ' + str(row['end_time'])
        tdelta = datetime.strptime(end_date, time_format) - datetime.strptime(start_date, time_format)
        hr_diff = tdelta.seconds / 3600

        if 4.0 <= hr_diff <= 24.0 and tdelta.days == 0:
            crisis_src.loc[15, curr_date] = crisis_src.loc[15, curr_date] + 1

    # sum the row
    crisis_src.loc[15, 'SFY 2021 Total'] = crisis_src.iloc[15, 4:16].sum()

    xl_writer = pd.ExcelWriter('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


r17()
