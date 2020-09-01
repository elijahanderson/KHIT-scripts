import pandas as pd
import time


def r30_48():
    filename = 'C:/Users/mingus/Documents/r30-48n.csv'

    df = pd.read_csv('C:/Users/mingus/Documents/r30-48.csv')
    df.sort_values(by=['full_name', 'actual_date'], inplace=True)
    df = df[df.duplicated(subset=['full_name'], keep=False)]
    df = df.reset_index()

    by_client = df.groupby('full_name')
    for client, frame in by_client:
        if 'Crisis Screening Services' not in frame['program_name'].values:
            df = df.drop(frame['program_name'].index)

    crisis_src = pd.read_excel('C:/Users/mingus/Documents/crisis_src.xlsx')
    crisis_src = crisis_src.rename(columns={
        'Name of Designated Screening Center: Oaks Integrated Care       \n\nCounty: Camden': 'desc'})
    # TODO -- insert current month, not aug_2020
    crisis_src.insert(loc=crisis_src.columns.get_loc('jun_2020') + 1, column='aug_2020', value=0)
    crisis_src.loc[44, 'desc'] = 'Involuntary Outpatient Commitment'

    for program in df['program_name']:
        if program != 'Crisis Screening Services':
            # TODO -- Go through program list on myEvolv to match the rest up
            if 'ICMS' in program:
                crisis_src.loc[34, 'aug_2020'] = crisis_src.loc[34, 'aug_2020'] + 1
            elif 'Involuntary Outpatient Commitment' in program:
                crisis_src.loc[44, 'aug_2020'] = crisis_src.loc[44, 'aug_2020'] + 1
            else:
                crisis_src.loc[45, 'aug_2020'] = crisis_src.loc[45, 'aug_2020'] + 1

    xl_writer = pd.ExcelWriter('C:/Users/mingus/Documents/crisis_src_2.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


r30_48()
