from datetime import datetime as dt
import pandas as pd
import time

def claim_details():
    filename = "C:/Users/mingus/Documents/" + str(dt.now().month) + "-" + str(dt.now().year) + "_claim_details.csv"
    
    claim_details_csv = pd.read_csv("C:/Users/mingus/Documents/claim_details.csv")
    services_csv = pd.read_csv("C:/Users/mingus/Documents/services.csv")

    claim_details_csv["full_name"] = (claim_details_csv["last_name"] + ", " + claim_details_csv["first_name"]).str.strip()
    services_csv["full_name"] = services_csv["full_name"].str.strip()
    
    services_csv["actual_date"] = pd.to_datetime(services_csv.actual_date).dt.date
    claim_details_csv["from_date"] = pd.to_datetime(claim_details_csv.from_date).dt.date
    claim_details_csv = claim_details_csv.rename(columns = {'from_date':'actual_date'})

    csv = claim_details_csv.merge(services_csv, on=["full_name", "actual_date"])
    csv = csv.drop_duplicates(keep=False)
    csv = csv[["invoice_number_x", "payor_name", "actual_date", "amount_expected", "total_amount_paid",
              "procedure_name", "procedure_code", "full_name", "staff_name"]]
    csv.sort_values(by=['payor_name', 'staff_name', 'procedure_code', 'actual_date',], inplace=True)
    
    csv.to_csv(filename, index=False)
    
    csv['amount_expected'] = csv['amount_expected'].replace('[\$]', '', regex=True).astype(float)
    csv['total_amount_paid'] = csv['total_amount_paid'].replace('[\$]', '', regex=True).astype(float)

    totals = csv.sum(axis=0, skipna=True)
    total_row = {'invoice_number_x': None, 'payor_name': None, 'actual_date': 'Totals:',
           'amount_expected': totals['amount_expected'], 'total_amount_paid': totals['total_amount_paid'],
           'procedure_name': None, 'procedure_code': None, 'full_name': None, 'staff_name': None}
    
    sums = csv.groupby('payor_name')['amount_expected','total_amount_paid'].sum()
    for idx, sum in sums.iterrows():
        row = {'invoice_number_x': None, 'payor_name': None, 'actual_date': idx + ' Subtotal:',
               'amount_expected': sums.loc[idx]['amount_expected'], 'total_amount_paid': sums.loc[idx]['total_amount_paid'],
               'procedure_name': None, 'procedure_code': None, 'full_name': None, 'staff_name': None}
        csv = csv.append(row, ignore_index=True)
        
    csv = csv.append(total_row, ignore_index=True)
    
    csv['amount_expected'] = csv['amount_expected'].apply(lambda val: '${:,.2f}'.format(val))
    csv['total_amount_paid'] = csv['total_amount_paid'].apply(lambda val: '${:,.2f}'.format(val))

    csv.to_csv(filename, index=False)
    

claim_details()
