import pandas as pd
from datetime import date, timedelta


def r21():
    """
        -- r21 --
        description:    Adults who have been discharged and readmitted to Crisis in fewer than 30 days.
        author notes:   Enrollment end dates include the previous as well as the current month due to the report
                        requirements.
    """
    df = pd.read_csv('C:/Users/mingus/Documents/r21.csv')

    curr_date = (date.today().replace(day=1) - timedelta(days=1)).strftime('%b_%Y').lower()
    crisis_src = pd.read_excel('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx')
    # set row 21 to the length of the df
    crisis_src.loc[19, curr_date] = len(df)
    # sum the row
    crisis_src.loc[19, 'SFY 2021 Total'] = crisis_src.iloc[19, 4:16].sum()

    xl_writer = pd.ExcelWriter('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


r21()
