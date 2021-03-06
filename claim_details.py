from datetime import date, timedelta
import pandas as pd


def claim_details():
    filename = "C:/Users/mingus/Documents/" + str((date.today().replace(day=1) - timedelta(days=1)).month) + "-" + str((date.today().replace(day=1) - timedelta(days=1)).year) + "_claim_details.csv"

    csv = pd.read_csv("C:/Users/mingus/Documents/claim_details.csv", engine='python')

    csv["client_name"] = csv["client_name"].str.strip()

    csv["from_date"] = pd.to_datetime(csv.from_date).dt.date
    csv = csv.rename(columns={'from_date': 'actual_date'})

    csv = csv[["invoice_number", "payor_name", "actual_date", "amount_expected", "total_amount_paid",
               "procedure_code", "client_name", "staff_name", "units", "rate_name"]]
    csv.sort_values(by=['payor_name', 'staff_name', 'procedure_code', 'actual_date', ], inplace=True)

    csv.to_csv(filename, index=False)

    csv['amount_expected'] = csv['amount_expected'].replace('[\$]', '', regex=True).astype(float)
    csv['total_amount_paid'] = csv['total_amount_paid'].replace('[\$]', '', regex=True).astype(float)

    totals = csv.sum(axis=0, skipna=True)
    total_row = {'invoice_number': None, 'payor_name': None, 'actual_date': 'Grand Totals:',
                 'amount_expected': totals['amount_expected'], 'total_amount_paid': totals['total_amount_paid'],
                 'procedure_code': None, 'client_name': None, 'staff_name': None}

    sums = csv.groupby(['payor_name', 'staff_name'])['amount_expected', 'total_amount_paid'].sum()
    payors = csv.payor_name.unique()

    csv = csv.append(pd.Series(), ignore_index=True)

    for payor in payors:
        irow = {'invoice_number': None, 'payor_name': payor, 'actual_date': 'Totals:',
                'amount_expected': sums.loc[payor]['amount_expected'].sum(),
                'total_amount_paid': sums.loc[payor]['total_amount_paid'].sum(),
                'procedure_code': None, 'client_name': None, 'staff_name': None}
        csv = csv.append(irow, ignore_index=True)
        for jdx, jsum in sums.loc[payor].iterrows():
            jrow = {'invoice_number': None, 'payor_name': payor, 'actual_date': jdx,
                    'amount_expected': jsum['amount_expected'], 'total_amount_paid': jsum['total_amount_paid'],
                    'procedure_code': None, 'client_name': None, 'staff_name': None}
            csv = csv.append(jrow, ignore_index=True)
        csv = csv.append({'invoice_number': None, 'payor_name': None, 'actual_date': None,
                          'amount_expected': None, 'total_amount_paid': None,
                          'procedure_code': None, 'client_name': None, 'staff_name': None}, ignore_index=True)

    csv = csv.append(pd.Series(), ignore_index=True)
    csv = csv.append(total_row, ignore_index=True)
    csv = csv.append(pd.Series(), ignore_index=True)

    csv['amount_expected'] = csv['amount_expected'].apply(lambda val: '${:,.2f}'.format(val))
    csv['total_amount_paid'] = csv['total_amount_paid'].apply(lambda val: '${:,.2f}'.format(val))
    csv = csv.replace('$nan', '')

    csv = csv.append({'invoice_number': None, 'payor_name': None, 'actual_date': 'Off-Site Services:',
                      'amount_expected': csv['rate_name'].value_counts()['TBS Off-Site 2018'],
                      'total_amount_paid': None, 'procedure_code': None, 'client_name': None, 'staff_name': None},
                     ignore_index=True)
    csv = csv.append({'invoice_number': None, 'payor_name': None, 'actual_date': 'On-Site Services:',
                      'amount_expected': csv['rate_name'].value_counts()['TBS On-Site 2018'],
                      'total_amount_paid': None, 'procedure_code': None, 'client_name': None, 'staff_name': None},
                     ignore_index=True)

    csv.to_csv(filename, index=False)


claim_details()
