import pandas as pd
from datetime import date


def r30_48():
    """
        -- r18-20 --
        description:    Adults with Substance Use, Cognitive, or Developmental Treatment Diagnoses
        author notes:
    """
    df = pd.read_csv('C:/Users/mingus/Documents/r30-48.csv')
    df.sort_values(by=['full_name', 'actual_date'], inplace=True)
    df = df[df.duplicated(subset=['full_name'], keep=False)]
    df = df.reset_index()

    by_client = df.groupby('full_name')
    for client, frame in by_client:
        if 'Crisis Screening Services' not in frame['program_name'].values:
            df = df.drop(frame['program_name'].index)

    crisis_src = pd.read_excel('crisis_sfy_2021.xlsx')
    curr_date = date.today().strftime('%b_%Y').lower()

    for program in df['program_name']:
        if program != 'Crisis Screening Services':
            if 'Jail' in program:
                crisis_src.loc[28, curr_date] = crisis_src.loc[28, curr_date] + 1
            elif 'EISS' in program:
                crisis_src.loc[29, curr_date] = crisis_src.loc[29, curr_date] + 1
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
            elif ('Oasis II' in program) or ('Homestretch' in program) or ('Children\'s Residential' in program) or \
                    ('Harvey\'s Haven' in program) or ('Medford Meadows' in program):
                crisis_src.loc[36, curr_date] = crisis_src.loc[36, curr_date] + 1
            elif 'PATH' in program:
                crisis_src.loc[37, curr_date] = crisis_src.loc[37, curr_date] + 1
            elif 'Justice Involved' in program:
                crisis_src.loc[38, curr_date] = crisis_src.loc[38, curr_date] + 1
            elif ('Strengthening Families' in program) or ('Behavioral Health Home' in program) or ('FPS' in program) \
                    or ('CHR-P' in program) or ('Mobile Response' in program) or ('Clinical In-Home' in program) \
                    or ('PACS' in program) or ('Coordinated Specialty' in program) or ('Oasis Ancora' in program) \
                    or ('CCBHC' in program) or ('Pat Lebon' in program) or ('Keeping Families' in program) \
                    or ('Crisis Diversion' in program) or ('Trauma Informed' in program) or ('IFSS' in program):
                crisis_src.loc[39, curr_date] = crisis_src.loc[39, curr_date] + 1
            # Nursing Facility /Assisted Living always 0
            elif ('Straight to Treatment' in program) or ('STAR' in program) or ('Addictions' in program) \
                    or ('Opioid' in program):
                crisis_src.loc[41, curr_date] = crisis_src.loc[41, curr_date] + 1
            # Veterans Admin Program always 0
            # Family always 0
            elif 'Involuntary Outpatient Commitment' in program:
                crisis_src.loc[44, curr_date] = crisis_src.loc[44, curr_date] + 1
            else:
                crisis_src.loc[45, curr_date] = crisis_src.loc[45, curr_date] + 1

    # sum each program
    for idx, row in crisis_src.loc[28:45, :].iterrows():
        crisis_src.loc[idx, 'SFY 2021 Total'] = row.iloc[4:16].sum()

    xl_writer = pd.ExcelWriter('crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


r30_48()
