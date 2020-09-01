import pandas as pd
from datetime import date


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

    crisis_src = pd.read_excel('C:/Users/mingus/Documents/crisis_sfy_2021.xlsx')
    crisis_src = crisis_src.rename(columns={
        'Name of Designated Screening Center: Oaks Integrated Care       \n\nCounty: Camden': 'desc'})
    curr_date = date.today().strftime('%b_%Y').lower()
    crisis_src.loc[44, 'desc'] = 'Involuntary Outpatient Commitment'

    for program in df['program_name']:
        if program != 'Crisis Screening Services':
            # TODO -- ask Oaks, cuz program names don't match up
            if 'Jail' in program:
                crisis_src.loc[28, curr_date] = crisis_src.loc[32, curr_date] + 1
            # Affiliated Emergency Services?
            elif 'IOTSS' in program:
                crisis_src.loc[30, curr_date] = crisis_src.loc[30, curr_date] + 1
            elif 'PACT' in program:
                crisis_src.loc[31, curr_date] = crisis_src.loc[31, curr_date] + 1
            elif 'Partial Care' in program:
                crisis_src.loc[32, curr_date] = crisis_src.loc[32, curr_date] + 1
            elif 'Adult Outpatient' in program:
                crisis_src.loc[33, curr_date] = crisis_src.loc[33, curr_date] + 1
            elif 'ICMS' in program:
                crisis_src.loc[34, curr_date] = crisis_src.loc[34, curr_date] + 1
            elif ('Supportive Housing' in program) or ('Housing Stabilization' in program) or \
                    ('Residential Intensive' in program):
                crisis_src.loc[35, curr_date] = crisis_src.loc[35, curr_date] + 1
            # Other DMHS Funded Residential Program (e.g. group home)?
            elif 'PATH' in program:
                crisis_src.loc[37, curr_date] = crisis_src.loc[37, curr_date] + 1
            elif 'Justice Involved' in program:
                crisis_src.loc[38, curr_date] = crisis_src.loc[38, curr_date] + 1
            # Other Mental Health Services?
            # Nursing Facility /Assisted Living?
            # Substance Abuse Program? (maybe Addictions)
            # Veterans Admin Program?
            # Family?
            elif 'Involuntary Outpatient Commitment' in program:
                crisis_src.loc[44, curr_date] = crisis_src.loc[44, curr_date] + 1
            else:
                crisis_src.loc[45, curr_date] = crisis_src.loc[45, curr_date] + 1

    # sum each program
    for idx, row in crisis_src.loc[28:45, :].iterrows():
        crisis_src.loc[idx, 'SFY 2021 Total'] = row.iloc[4:16].sum()

    xl_writer = pd.ExcelWriter('C:/Users/mingus/Documents/crisis_sfy_2021_2.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


r30_48()
