import pandas as pd
from datetime import date, datetime


def r17():
    df = pd.read_csv('C:/Users/mingus/Documents/r17.csv')
    df.sort_values(by=['full_name', 'actual_date'], inplace=True)
    df = df.reset_index(drop=True)

    df["actual_date"] = pd.to_datetime(df.actual_date)
    df["end_date"] = pd.to_datetime(df.end_date)
    df = df.rename(columns={'actual_date.1': 'start_time', 'end_date.1':'end_time'})

    curr_date = date.today().strftime('%b_%Y').lower()
    crisis_src = pd.read_excel('crisis_sfy_2021.xlsx')
    time_format = '%Y-%m-%d %I:%M %p'

    for idx, row in df.iterrows():
        start_date = str(row['actual_date'])[0:10] + ' ' + str(row['start_time'])
        end_date = str(row['end_date'])[0:10] + ' ' + str(row['end_time'])
        tdelta = datetime.strptime(end_date, time_format) - \
                 datetime.strptime(start_date, time_format)
        hr_diff = tdelta.seconds / 3600

        if 4.0 <= hr_diff <= 24.0 and tdelta.days == 0:
            crisis_src.loc[15, curr_date] = crisis_src.loc[15, curr_date] + 1

    # sum the row
    crisis_src.loc[15, 'SFY 2021 Total'] = crisis_src.iloc[15, 4:16].sum()

    xl_writer = pd.ExcelWriter('crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


r17()