import pandas as pd
from datetime import date, timedelta


def r30_48():
    """
        -- r30-48 --
        description:    Adults admitted to Crisis in current month who are also enrolled in other programs/services
        author notes:
    """
    df = pd.read_csv('C:/Users/mingus/Documents/r30-48.csv')
    df = df.rename(columns={'Other Programs': 'program', 'USTF Emergency Screening #28': 'answer_val'})

    crisis_src = pd.read_excel('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx')
    curr_date = (date.today().replace(day=1) - timedelta(days=1)).strftime('%b_%Y').lower()

    program_list = ['Jail', 'EISS', 'IOTSS', 'PACT', 'Partial Care', 'Adult Outpatient', 'ICMS', 'Supportive Housing',
                    'Housing Stabilization', 'Residential Intensive', 'Oasis II', 'Homestretch',
                    'Children\'s Residential', 'Harvey\'s Haven', 'Medford Meadows', 'PATH', 'Justice Involved',
                    'Strengthening Families', 'Behavioral Health Home', 'FPS', 'CHR-P', 'Mobile Response',
                    'Clinical In-Home', 'PACS', 'Coordinated Specialty', 'Oasis Ancora', 'CCBHC', 'Pat Lebon',
                    'Keeping Families', 'Crisis Diversion', 'Trauma Informed', 'IFSS', 'Straight to Treatment',
                    'STAR', 'Addictions', 'Opioid', 'Involuntary Outpatient Commitment']

    for idx, row in df.iterrows():
        if pd.isna(row['answer_val']):
            row['answer_val'] = ''
        if pd.isna(row['program']):
            row['program'] = ''
        if 'Jail' in row['program'] or row['answer_val'] == 'Probation':
            crisis_src.loc[28, curr_date] = crisis_src.loc[28, curr_date] + 1
        elif 'EISS' in row['program'] or row['answer_val'] == 'Emergency/Mobile/Outreach Treatment Team':
            crisis_src.loc[29, curr_date] = crisis_src.loc[29, curr_date] + 1
        elif 'IOTSS' in row['program']:
            crisis_src.loc[30, curr_date] = crisis_src.loc[30, curr_date] + 1
        elif 'PACT' in row['program']:
            crisis_src.loc[31, curr_date] = crisis_src.loc[31, curr_date] + 1
        elif 'Partial Care' in row['program'] or row['answer_val'] == 'Partial Care':
            crisis_src.loc[32, curr_date] = crisis_src.loc[32, curr_date] + 1
        elif 'Adult Outpatient' in row['program'] or row['answer_val'] == 'Outpatient/Counseling':
            crisis_src.loc[33, curr_date] = crisis_src.loc[33, curr_date] + 1
        elif 'ICMS' in row['program']:
            crisis_src.loc[34, curr_date] = crisis_src.loc[34, curr_date] + 1
        elif (('Supportive Housing' in row['program'])
              or ('Housing Stabilization' in row['program'])
              or ('Residential Intensive' in row['program'])
              or (row['answer_val'] == 'Residential Care')
              or (row['answer_val'] == 'Supportive Housing (e.g. RIST)')):
            crisis_src.loc[35, curr_date] = crisis_src.loc[35, curr_date] + 1
        elif (('Oasis II' in row['program'])
              or ('Homestretch' in row['program'])
              or ('Children\'s Residential' in row['program'])
              or ('Harvey\'s Haven' in row['program'])
              or ('Medford Meadows' in row['program'])
              or (row['answer_val'] == 'Group Homes with MH Services')):
            crisis_src.loc[36, curr_date] = crisis_src.loc[36, curr_date] + 1
        elif 'PATH' in row['program']:
            crisis_src.loc[37, curr_date] = crisis_src.loc[37, curr_date] + 1
        elif (('Justice Involved' in row['program'])
              or ('Correction' in row['answer_val'])
              or (row['answer_val'] == 'Justice Involved Services')
              or (row['answer_val'] == 'Detention Center')):
            crisis_src.loc[38, curr_date] = crisis_src.loc[38, curr_date] + 1
        elif(('Strengthening Families' in row['program'])
             or ('Behavioral Health Home' in row['program'])
             or ('FPS' in row['program'])
             or ('CHR-P' in row['program'])
             or ('Mobile Response' in row['program'])
             or ('Clinical In-Home' in row['program'])
             or ('PACS' in row['program'])
             or ('Coordinated Specialty' in row['program'])
             or ('Oasis Ancora' in row['program'])
             or ('CCBHC' in row['program'])
             or ('Pat Lebon' in row['program'])
             or ('Keeping Families' in row['program'])
             or ('Crisis Diversion' in row['program'])
             or ('Trauma Informed' in row['program'])
             or ('IFSS' in row['program'])
             or (row['answer_val'] == 'Other Mental Health Services (e.g. private practitioner)')):
            crisis_src.loc[39, curr_date] = crisis_src.loc[39, curr_date] + 1
        elif row['answer_val'] == 'Nursing Facility/Assisted Living':
            crisis_src.loc[40, curr_date] = crisis_src.loc[40, curr_date] + 1
        elif (('Straight to Treatment' in row['program'])
              or ('STAR' in row['program'])
              or ('Addictions' in row['program'])
              or ('Opioid' in row['program'])
              or (row['answer_val'] == 'Drug Treatment Program')):
            crisis_src.loc[41, curr_date] = crisis_src.loc[41, curr_date] + 1
        # veterans admin program always 0
        elif row['answer_val'] == 'Family Crisis Intervention Unit (FCIU)':
            crisis_src.loc[43, curr_date] = crisis_src.loc[43, curr_date] + 1
        elif (('Involuntary Outpatient Commitment' in row['program'])
              or (row['answer_val'] == 'Family Crisis Intervention Unit (FCIU)')):
            crisis_src.loc[44, curr_date] = crisis_src.loc[44, curr_date] + 1
        # if all the other categories have been checked, the program is uncategorized
        elif not (any(row['program'] in iprogram for iprogram in program_list)
                  or any(iprogram in row['program'] for iprogram in program_list)):
            crisis_src.loc[45, curr_date] = crisis_src.loc[45, curr_date] + 1
        # 'None' row always 0

    # sum each row
    for idx, row in crisis_src.loc[28:45, :].iterrows():
        crisis_src.loc[idx, 'SFY 2021 Total'] = row.iloc[4:16].sum()

    xl_writer = pd.ExcelWriter('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


r30_48()
