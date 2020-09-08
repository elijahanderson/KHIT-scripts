import pandas as pd
from datetime import date
import time


def r18_20():
    df = pd.read_csv('C:/Users/mingus/Documents/r18-20.csv')
    df.sort_values(by=['full_name'], inplace=True)

    curr_date = date.today().strftime('%b_%Y').lower()
    crisis_src = pd.read_excel('crisis_sfy_2021.xlsx')

    df = df.rename(columns={'ICD9_ Code': 'category'})

    df['category'] = df['category'].apply(categorize)

    for cat in df['category']:
        if cat == 'Dementia/Cognitive Disorder':
            crisis_src.loc[17, curr_date] = crisis_src.loc[17, curr_date] + 1

    # sum each program
    for idx, row in crisis_src.loc[16:20, :].iterrows():
        crisis_src.loc[idx, 'SFY 2021 Total'] = row.iloc[4:16].sum()

    xl_writer = pd.ExcelWriter('crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


def categorize(code):
    if code == '295.80':
        return 'Dementia/Cognitive Disorder'
    else:
        return code


r18_20()
