import pandas as pd
from datetime import date


def r21():
    df = pd.read_csv('C:/Users/mingus/Documents/r21.csv')
    df["actual_date"] = pd.to_datetime(df.actual_date)
    df["end_date"] = pd.to_datetime(df.end_date)
    df.sort_values(by=['full_name', 'actual_date'], inplace=True)
    df = df[df.duplicated(subset=['full_name'], keep=False)]
    df = df.reset_index()
    df = df[['full_name', 'program_name', 'actual_date', 'end_date']]

    by_client = df.groupby('full_name')
    curr_date = date.today().strftime('%b_%Y').lower()
    crisis_src = pd.read_excel('crisis_sfy_2021.xlsx')

    for client, frame in by_client:
        frame = frame.tail(2)
        frame = frame.reset_index()
        date_diff = int(str(frame.loc[1, 'actual_date'] - frame.loc[0, 'end_date']).split(' ')[0])
        if date_diff < 30:  # TODO -- might need to elaborate condition
            crisis_src.loc[19, curr_date] = crisis_src.loc[19, curr_date] + 1

    xl_writer = pd.ExcelWriter('crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


r21()
