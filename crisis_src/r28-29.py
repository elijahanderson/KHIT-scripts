import pandas as pd
from datetime import date, timedelta


def r28_29():
    """
        -- r18-20 --
        description:    Adults with a Crisis Triage event and Outreach event within 1-2 or > 2 hours of each other
        author notes:
    """
    df = pd.read_csv('C:/Users/mingus/Documents/r28-29.csv')
    df = df.rename(columns={'Time Between Entry and Adult Intake (Mins)': 'time_diff'})

    curr_date = (date.today().replace(day=1) - timedelta(days=1)).strftime('%b_%Y').lower()
    crisis_src = pd.read_excel('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx')

    for idx, row in df.iterrows():
        if row['SecureStatus'] == 'Secured':
            crisis_src.loc[27, curr_date] = crisis_src.loc[27, curr_date] + 1
        elif row['SecureStatus'] == 'Unsecured':
            crisis_src.loc[26, curr_date] = crisis_src.loc[26, curr_date] + 1

    # sum each program
    for idx, row in crisis_src.loc[26:27, :].iterrows():
        crisis_src.loc[idx, 'SFY 2021 Total'] = row.iloc[4:16].sum()

    xl_writer = pd.ExcelWriter('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


r28_29()
