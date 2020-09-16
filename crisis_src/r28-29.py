import pandas as pd
from datetime import date, datetime


def r28_29():
    """
        -- r18-20 --
        description:    Adults with a Crisis Triage event and Outreach event within 1-2 or > 2 hours of each other
        author notes:   Not a single client that meets specified criteria. Should probably ask Oaks about it.
    """
    df = pd.read_csv('C:/Users/mingus/Documents/r28-29.csv')
    df.sort_values(by=['full_name', 'actual_date'], inplace=True)
    df = df[df.duplicated(subset=['full_name'], keep=False)]
    df = df.reset_index(drop=True)
    # convert to pd datetime for date operations
    df["actual_date"] = pd.to_datetime(df.actual_date)
    # rename for legibility
    df = df.rename(columns={'actual_date': 'date', 'actual_date.1': 'time'})

    by_client = df.groupby('full_name')
    curr_date = date.today().strftime('%b_%Y').lower()
    crisis_src = pd.read_excel('crisis_sfy_2021.xlsx')
    time_format = '%I:%M %p'

    # for each client
    for client, frame in by_client:
        frame = frame.reset_index(drop=True)
        # if they have both events
        if 'Outreach' in frame.event_name.unique() and 'Crisis Triage' in frame.event_name.unique():
            for idx, row in frame.iterrows():
                if (idx+1) < len(frame):
                    # look at two rows at a time, and if their date is the same but event is different, then increment
                    # the appropriate row according to the time difference (1-2 or >=2 hours)
                    if row['date'] == frame.loc[idx+1, 'date'] and row['event_name'] != frame.loc[idx+1, 'event_name']:
                        tdelta = datetime.strptime(row['time'], time_format) - \
                                 datetime.strptime(frame.loc[idx+1, 'time'], time_format)
                        hr_diff = tdelta.seconds / 3600
                        # between 1 & 2 hours
                        if hr_diff >= 1.0 or hr_diff < 2.0:
                            crisis_src.loc[26, curr_date] = crisis_src.loc[26, curr_date] + 1
                        # over 2 hours
                        elif hr_diff >= 2.0:
                            crisis_src.loc[27, curr_date] = crisis_src.loc[27, curr_date] + 1

    # sum each program
    for idx, row in crisis_src.loc[26:27, :].iterrows():
        crisis_src.loc[idx, 'SFY 2021 Total'] = row.iloc[4:16].sum()

    xl_writer = pd.ExcelWriter('crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


r28_29()
