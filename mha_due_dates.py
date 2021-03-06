from datetime import date, timedelta
import pandas as pd


def mha_due_dates():
    mha_csv = pd.read_csv("C:/Users/mingus/Documents/mha_due_dates.csv")
    staff_csv = pd.read_csv("C:/Users/mingus/Documents/direct_staff.csv")

    mha_csv = mha_csv.rename(columns={'Full Name': 'name'})
    mha_csv['name'] = mha_csv['name'].str.strip()
    staff_csv['name'] = staff_csv['name'].str.strip()
    staff_csv = staff_csv[['name', 'id_no', 'worker_name', 'worker_role']]

    merged = mha_csv.merge(staff_csv, on='name')
    merged['due_date'] = pd.to_datetime(merged.due_date)
    merged.sort_values(by=['name', 'due_date'], inplace=True, ascending=[True, True])

    merged.to_csv("C:/Users/mingus/Documents/" + str((date.today().replace(day=1) + timedelta(days=31)).month) + "-" +
                  str((date.today().replace(day=1) + timedelta(days=62)).month) + "-" +
                  str((date.today().replace(day=1) + timedelta(days=62)).year) + "_mha_due_dates.csv", index=False)


mha_due_dates()
