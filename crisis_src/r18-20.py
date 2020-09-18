import numpy as np
import pandas as pd
from datetime import date


def r18_20():
    """
        -- r18-20 --
        description:    Adults in Crisis with Substance Use, Cognitive, or Developmental Treatment Diagnoses
        author notes:
    """
    df = pd.read_csv('C:/Users/mingus/Documents/r18-20.csv')
    # drop all clients less than 18 y/o
    today = date.today().strftime('%Y-%m-%d')
    df["dob"] = pd.to_datetime(df.dob)
    df['dob'] = df['dob'].apply(lambda dob: (pd.to_datetime(today) - dob) / np.timedelta64(1, 'Y'))
    df = df[df['dob'] > 18]
    df.sort_values(by=['full_name'], inplace=True)

    df = df.rename(columns={'ICD9_ Code': 'category'})

    curr_date = date.today().strftime('%b_%Y').lower()
    crisis_src = pd.read_excel('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx')

    df['category'] = df['category'].apply(categorize)

    by_category = df.groupby('category')

    for category, frame in by_category:
        if category == 'Substance Abuse Disorder':
            crisis_src.loc[16, curr_date] = len(frame)
        elif category == 'Dementia/Cognitive Disorder':
            crisis_src.loc[17, curr_date] = len(frame)
        elif category == 'Developmental Disability':
            crisis_src.loc[18, curr_date] = len(frame)

    # sum each program
    for idx, row in crisis_src.loc[16:18, :].iterrows():
        crisis_src.loc[idx, 'SFY 2021 Total'] = row.iloc[4:16].sum()

    xl_writer = pd.ExcelWriter('D:/KHIT docs/KHIT-scripts/crisis_src/crisis_sfy_2021.xlsx', engine='xlsxwriter')
    crisis_src.to_excel(xl_writer, sheet_name='crisis_src', index=False)
    xl_writer.save()


def categorize(code):
    """
    Converts the Diagnosis ICD-9 codes to provided categories.
    :param code: The ICD-9 code of the client's diagnosis
    :return: The appropriate diagnosis category
    """
    icd10_codes = {
        'SAD': ['305', '305.01', '305.02', '305.03', '291.89', '291.82', '303.9', '303.91', '303.92', '303.93',
                '303', '303.01', '303.02', '303.03', '291', '291.81', '291.89', '291.2', '291.89', '291.82', '291.4',
                '291.5', '291.3', '291.1', '291.9', '305.5', '305.51', '305.52', '305.53', '292.89', '292.85', '304',
                '304.01', '304.02', '304.03', '292.85', '305.2', '305.21', '305.22', '305.23', '292.89', '304.3',
                '304.31', '304.32', '304.33', '305.4', '305.41', '305.42', '305.43', '304.1', '304.11', '304.12',
                '304.13', '305.6', '305.61', '305.62', '305.63', '304.2', '304.21', '304.23', '305.7', '305.71',
                '305.72', '305.73', '292.11', '292.12', '292.81', '292.2', '292.84', '292.9', '304.4', '304.41',
                '304.42', '304.43' '292', '305.3', '305.31', '305.32', '305.33', '304.5', '304.51', '304.52',
                '304.53', '305.1', '305.9', '305.91', '305.92', '305.93', '304.6', '304.61', '304.62', '304.63',
                '305.8', '305.81', '305.82', '305.83', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18',
                'F19'],
        'DD': ['317', '318', '318.1', '318.2', '319', '315.35', '315.39', '315.31', '315.32', '315.34', '315.9',
               '315.09', '315.2', '315.1', '315.01', 'V40.0', '315.4', '299.8', '299.81', '299', '299.01', '299.1',
               '299.9', '330.9', '315.8', 'F70', 'F71', 'F72', 'F73', 'F78', 'F79', 'F80', 'F81', 'F82', 'F84', 'F88',
               'F89'],
        'DCD': ['331.83', '780.99', '780.97', '293', '293.1', 'G31.84', 'R41.9', 'F05']
    }

    if code in icd10_codes['SAD'] or any(icode in code for icode in icd10_codes['SAD']):
        return 'Substance Abuse Disorder'
    elif code in icd10_codes['DCD'] or any(icode in code for icode in icd10_codes['SAD']):
        return 'Dementia/Cognitive Disorder'
    elif code in icd10_codes['DD'] or any(icode in code for icode in icd10_codes['SAD']):
        return 'Developmental Disability'


r18_20()
