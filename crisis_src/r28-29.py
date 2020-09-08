import pandas as pd
from datetime import date


def r28_29():
    df = pd.read_csv('C:/Users/mingus/Documents/r28-29.csv')
    df.sort_values(by=['full_name', 'actual_date'], inplace=True)
    # df = df[df.duplicated(subset=['full_name'], keep=False)]
    # df = df.reset_index()
    df["actual_date"] = pd.to_datetime(df.actual_date)

    print(df)

    by_client = df.groupby('full_name')
    curr_date = date.today().strftime('%b_%Y').lower()
    crisis_src = pd.read_excel('crisis_sfy_2021.xlsx')

    for client, frame in by_client:
        frame = frame.reset_index()


r28_29()
