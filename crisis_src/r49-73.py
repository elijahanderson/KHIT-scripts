import pandas as pd
from datetime import date


def r49_73():
    """
        -- r49-73 --
        description:    Adults discharged from Crisis to either a hospital (49-54) or the community (55-74),
                        filtered into rows by hospital discharged to / community program enrolled in.
        author notes:
    """
    df = pd.read_csv('C:/Users/mingus/Documents/r49-73.csv')
    df.sort_values(by=['full_name', 'actual_date'], inplace=True)
    df = df.reset_index(drop=True)

    crisis_src = pd.read_excel('crisis_sfy_2021.xlsx')
    curr_date = date.today().strftime('%b_%Y').lower()

    # for each discharge instance
    for idx, row in df.iterrows():
        # need to track clients checked since there may be duplicate discharge instances for the same client
        clients_checked = []
        if not row['full_name'] in clients_checked:
            # if they have been discharged to a hospital, increment the appropriate hospital category row by 1
            if 'Hospital' in str(row['discharged_to_location_desc']):
                # TODO -- will have to finish hospital categorization later once I have the category list
                # county hospital
                if 'Cooper Hospital' in row['discharged_to_location_desc']:
                    crisis_src.loc[50, curr_date] = crisis_src.loc[50, curr_date] + 1
                # state hospital
                if 'Kennedy Memorial Hospital' in row['discharged_to_location_desc']:
                    crisis_src.loc[51, curr_date] = crisis_src.loc[51, curr_date] + 1

            # otherwise, if a client was enrolled in another program by the end of current month,
            # increment appropriate row by 1
            else:
                programs_df = pd.read_csv('C:/Users/mingus/Documents/programs_csv.csv')
                client_programs = programs_df.loc[programs_df['full_name'] == row['full_name']]
                client_programs = client_programs['program_name'].unique()
                program_list = ['Jail', 'EISS', 'IOTSS', 'PACT', 'Partial Care', 'Adult Outpatient', 'ICMS',
                                'Supportive Housing',
                                'Housing Stabilization', 'Residential Intensive', 'Oasis II', 'Homestretch',
                                'Children\'s Residential', 'Harvey\'s Haven', 'Medford Meadows', 'PATH',
                                'Justice Involved',
                                'Strengthening Families', 'Behavioral Health Home', 'FPS', 'CHR-P', 'Mobile Response',
                                'Clinical In-Home', 'PACS', 'Coordinated Specialty', 'Oasis Ancora', 'CCBHC',
                                'Pat Lebon',
                                'Keeping Families', 'Crisis Diversion', 'Trauma Informed', 'IFSS',
                                'Straight to Treatment',
                                'STAR', 'Addictions', 'Opioid', 'Involuntary Outpatient Commitment']
                categories_checked = []
                for program in client_programs:
                    if program != 'Crisis Screening Services':
                        if 'Jail' in program and 53 not in categories_checked:
                            crisis_src.loc[53, curr_date] = crisis_src.loc[53, curr_date] + 1
                            categories_checked.append(53)
                        elif 'EISS' in program and 54 not in categories_checked:
                            crisis_src.loc[54, curr_date] = crisis_src.loc[54, curr_date] + 1
                            categories_checked.append(54)
                        elif 'IOTSS' in program and 55 not in categories_checked:
                            crisis_src.loc[55, curr_date] = crisis_src.loc[55, curr_date] + 1
                            categories_checked.append(55)
                        elif 'PACT' in program and 56 not in categories_checked:
                            crisis_src.loc[56, curr_date] = crisis_src.loc[56, curr_date] + 1
                            categories_checked.append(56)
                        elif 'Partial Care' in program and 57 not in categories_checked:
                            crisis_src.loc[57, curr_date] = crisis_src.loc[57, curr_date] + 1
                            categories_checked.append(57)
                        elif 'Adult Outpatient' in program and 58 not in categories_checked:
                            crisis_src.loc[58, curr_date] = crisis_src.loc[58, curr_date] + 1
                            categories_checked.append(58)
                        elif 'ICMS' in program and 59 not in categories_checked:
                            crisis_src.loc[59, curr_date] = crisis_src.loc[59, curr_date] + 1
                            categories_checked.append(59)
                        elif (('Supportive Housing' in program)
                              or ('Housing Stabilization' in program)
                              or ('Residential Intensive' in program)) \
                                and 60 not in categories_checked:
                            crisis_src.loc[60, curr_date] = crisis_src.loc[60, curr_date] + 1
                            categories_checked.append(60)
                        elif (('Oasis II' in program)
                              or ('Homestretch' in program)
                              or ('Children\'s Residential' in program)
                              or ('Harvey\'s Haven' in program)
                              or ('Medford Meadows' in program)) \
                                and 61 not in categories_checked:
                            crisis_src.loc[61, curr_date] = crisis_src.loc[61, curr_date] + 1
                            categories_checked.append(61)
                        elif 'PATH' in program and 62 not in categories_checked:
                            crisis_src.loc[62, curr_date] = crisis_src.loc[62, curr_date] + 1
                            categories_checked.append(62)
                        elif 'Justice Involved' in program and 63 not in categories_checked:
                            crisis_src.loc[63, curr_date] = crisis_src.loc[63, curr_date] + 1
                            categories_checked.append(63)
                        elif (('Strengthening Families' in program)
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
                                and 64 not in categories_checked:
                            crisis_src.loc[64, curr_date] = crisis_src.loc[64, curr_date] + 1
                            categories_checked.append(64)
                        # Nursing Facility /Assisted Living always 0
                        elif (('Straight to Treatment' in program)
                              or ('STAR' in program)
                              or ('Addictions' in program)
                              or ('Opioid' in program)) \
                                and 66 not in categories_checked:
                            crisis_src.loc[66, curr_date] = crisis_src.loc[66, curr_date] + 1
                            categories_checked.append(66)
                        # Veterans Admin Program always 0
                        # Family always 0
                        elif 'Involuntary Outpatient Commitment' in program and 69 not in categories_checked:
                            crisis_src.loc[69, curr_date] = crisis_src.loc[69, curr_date] + 1
                            categories_checked.append(69)
                        # if all the other categories have been checked, the program is uncategorized
                        elif (not (any(program in iprogram for iprogram in program_list)
                                   or any(iprogram in program for iprogram in program_list))) \
                                and 70 not in categories_checked:
                            crisis_src.loc[70, curr_date] = crisis_src.loc[70, curr_date] + 1
                            categories_checked.append(70)
                    # if client was incarcerated after discharge
                    elif len(client_programs) < 2 and row['closing_reason'] == 'Incarceration' \
                            and 53 not in categories_checked:
                        crisis_src.loc[53, curr_date] = crisis_src.loc[53, curr_date] + 1
                        categories_checked.append(53)
                    # if closing reason indicates another program but client not yet enrolled, put under Other
                    elif len(client_programs) < 2 and ('Referral' in row['closing_reason']
                                                       or 'Transfer' in row['closing_reason']
                                                       or 'Referred' in row['closing_reason']
                                                       or 'Referred' in row['closing_reason']) \
                            and 70 not in categories_checked:
                        crisis_src.loc[70, curr_date] = crisis_src.loc[70, curr_date] + 1
                        categories_checked.append(70)
                    # if closing reason indicates
                    elif len(client_programs) < 2 and 'Involuntarily' in row['closing_reason'] \
                            and 49 not in categories_checked:
                        crisis_src.loc[49, curr_date] = crisis_src.loc[49, curr_date] + 1
                        categories_checked.append(49)
                    # None if client was not enrolled in any other program as of current month and
                    # closing reason doesn't indicate they were referred to another program or hospitalized
                    elif len(client_programs) < 2 and 71 not in categories_checked:
                        crisis_src.loc[71, curr_date] = crisis_src.loc[71, curr_date] + 1

        clients_checked.append(row['full_name'])

    # sum the total discharges to hospital, then total discharges to community
    crisis_src.loc[52, curr_date] = crisis_src.loc[47:51, curr_date].sum()
    crisis_src.loc[72, curr_date] = crisis_src.loc[53:71, curr_date].sum()

    # sum each client_programs
    for idx, row in crisis_src.loc[47:72, :].iterrows():
        crisis_src.loc[idx, 'SFY 2021 Total'] = row.iloc[4:16].sum()

    xl_writer = pd.ExcelWriter('crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


r49_73()
