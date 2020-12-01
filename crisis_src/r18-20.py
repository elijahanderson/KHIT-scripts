import pandas as pd
from datetime import date, timedelta


def r18_20():
    """
        -- r18-20 --
        description:    Adults in Crisis with Substance Use, Cognitive, or Developmental Treatment Diagnoses
        author notes:
    """
    df = pd.read_csv('C:/Users/mingus/Documents/r18-20.csv')

    curr_date = (date.today().replace(day=1) - timedelta(days=1)).strftime('%b_%Y').lower()
    crisis_src = pd.read_excel('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx')

    for idx, row in df.iterrows():
        if row['Row'] == 'Row 18':
            crisis_src.loc[16, curr_date] = crisis_src.loc[16, curr_date] + 1
        elif row['Row'] == 'Row 19':
            crisis_src.loc[17, curr_date] = crisis_src.loc[16, curr_date] + 1
        elif row['Row'] == 'Row 20':
            crisis_src.loc[18, curr_date] = crisis_src.loc[18, curr_date] + 1

    # sum each program
    for idx, row in crisis_src.loc[16:18, :].iterrows():
        crisis_src.loc[idx, 'SFY 2021 Total'] = row.iloc[4:16].sum()

    xl_writer = pd.ExcelWriter('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


r18_20()
