import pandas as pd
from datetime import date


def r30_48():
    """
        -- r30-48 --
        description:    Adults admitted to Crisis in current month who are also enrolled in other client_programss/services
        author notes:
    """
    df = pd.read_csv('C:/Users/mingus/Documents/r30-48.csv')
    df.sort_values(by=['full_name', 'actual_date'], inplace=True)
    # drop clients only enrolled in one client_programs
    df = df[df.duplicated(subset=['full_name'], keep=False)]
    df = df.reset_index()

    # drop all clients not enrolled in Crisis
    by_client = df.groupby('full_name')
    for client, frame in by_client:
        if 'Crisis Screening Services' not in frame['program_name'].values:
            df = df.drop(frame['program_name'].index)

    crisis_src = pd.read_excel('crisis_sfy_2021.xlsx')
    curr_date = date.today().strftime('%b_%Y').lower()
    program_list = ['Jail', 'EISS', 'IOTSS', 'PACT', 'Partial Care', 'Adult Outpatient', 'ICMS', 'Supportive Housing',
                    'Housing Stabilization', 'Residential Intensive', 'Oasis II', 'Homestretch',
                    'Children\'s Residential', 'Harvey\'s Haven', 'Medford Meadows', 'PATH', 'Justice Involved',
                    'Strengthening Families', 'Behavioral Health Home', 'FPS', 'CHR-P', 'Mobile Response',
                    'Clinical In-Home', 'PACS', 'Coordinated Specialty', 'Oasis Ancora', 'CCBHC', 'Pat Lebon',
                    'Keeping Families', 'Crisis Diversion', 'Trauma Informed', 'IFSS', 'Straight to Treatment',
                    'STAR', 'Addictions', 'Opioid', 'Involuntary Outpatient Commitment']

    # for each client, if they are enrolled in a client_programs other than Crisis, increment the appropriate row by 1
    by_client = df.groupby('full_name')
    for client, frame in by_client:
        client_programs = frame['program_name'].unique()
        categories_checked = []
        for program in client_programs:
            if program != 'Crisis Screening Services':
                if 'Jail' in program and 28 not in categories_checked:
                    crisis_src.loc[28, curr_date] = crisis_src.loc[28, curr_date] + 1
                    categories_checked.append(28)
                elif 'EISS' in program and 29 not in categories_checked:
                    crisis_src.loc[29, curr_date] = crisis_src.loc[29, curr_date] + 1
                    categories_checked.append(29)
                elif 'IOTSS' in program and 30 not in categories_checked:
                    crisis_src.loc[30, curr_date] = crisis_src.loc[30, curr_date] + 1
                    categories_checked.append(30)
                elif 'PACT' in program and 31 not in categories_checked:
                    crisis_src.loc[31, curr_date] = crisis_src.loc[31, curr_date] + 1
                    categories_checked.append(31)
                elif 'Partial Care' in program and 32 not in categories_checked:
                    crisis_src.loc[32, curr_date] = crisis_src.loc[32, curr_date] + 1
                    categories_checked.append(32)
                elif 'Adult Outpatient' in program and 33 not in categories_checked:
                    crisis_src.loc[33, curr_date] = crisis_src.loc[33, curr_date] + 1
                    categories_checked.append(33)
                elif 'ICMS' in program and 34 not in categories_checked:
                    crisis_src.loc[34, curr_date] = crisis_src.loc[34, curr_date] + 1
                    categories_checked.append(34)
                elif (('Supportive Housing' in program)
                      or ('Housing Stabilization' in program)
                      or ('Residential Intensive' in program)) \
                        and 35 not in categories_checked:
                    crisis_src.loc[35, curr_date] = crisis_src.loc[35, curr_date] + 1
                    categories_checked.append(35)
                elif (('Oasis II' in program)
                      or ('Homestretch' in program)
                      or ('Children\'s Residential' in program)
                      or ('Harvey\'s Haven' in program)
                      or ('Medford Meadows' in program)) \
                        and 36 not in categories_checked:
                    crisis_src.loc[36, curr_date] = crisis_src.loc[36, curr_date] + 1
                    categories_checked.append(36)
                elif 'PATH' in program and 37 not in categories_checked:
                    crisis_src.loc[37, curr_date] = crisis_src.loc[37, curr_date] + 1
                    categories_checked.append(37)
                elif 'Justice Involved' in program and 38 not in categories_checked:
                    crisis_src.loc[38, curr_date] = crisis_src.loc[38, curr_date] + 1
                    categories_checked.append(38)
                elif(('Strengthening Families' in program)
                     or ('Behavioral Health Home' in program)
                     or ('FPS' in program)
                     or ('CHR-P' in program)
                     or ('Mobile Response' in program)
                     or ('Clinical In-Home' in program)
                     or ('PACS' in program)
                     or ('Coordinated Specialty' in program)
                     or ('Oasis Ancora' in program)
                     or ('CCBHC' in program)
                     or ('Pat Lebon' in program)
                     or ('Keeping Families' in program)
                     or ('Crisis Diversion' in program)
                     or ('Trauma Informed' in program)
                     or ('IFSS' in program)) \
                        and 39 not in categories_checked:
                    crisis_src.loc[39, curr_date] = crisis_src.loc[39, curr_date] + 1
                    categories_checked.append(39)
                # Nursing Facility /Assisted Living always 0
                elif (('Straight to Treatment' in program)
                      or ('STAR' in program)
                      or ('Addictions' in program)
                      or ('Opioid' in program)) \
                        and 41 not in categories_checked:
                    crisis_src.loc[41, curr_date] = crisis_src.loc[41, curr_date] + 1
                    categories_checked.append(41)
                # Veterans Admin Program always 0
                # Family always 0
                elif 'Involuntary Outpatient Commitment' in program and 44 not in categories_checked:
                    crisis_src.loc[44, curr_date] = crisis_src.loc[44, curr_date] + 1
                    categories_checked.append(44)
                # if all the other categories have been checked, the program is uncategorized
                elif not (any(program in iprogram for iprogram in program_list)
                          or any(iprogram in program for iprogram in program_list)):
                    crisis_src.loc[45, curr_date] = crisis_src.loc[45, curr_date] + 1
                    categories_checked.append(45)

    # sum each program
    for idx, row in crisis_src.loc[28:45, :].iterrows():
        crisis_src.loc[idx, 'SFY 2021 Total'] = row.iloc[4:16].sum()

    xl_writer = pd.ExcelWriter('crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


r30_48()
