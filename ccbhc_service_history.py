from datetime import datetime as dt
import pandas as pd


def ccbhc_service_history():
    filename = "C:/Users/mingus/Documents/" + str(dt.now().month) + "-" + str(dt.now().year) + "_service_history.csv"

    service_history_csv = pd.read_csv("C:/Users/mingus/Documents/ccbhc_service_history.csv")
    payors_csv = pd.read_csv("C:/Users/mingus/Documents/ccbhc_payors.csv")

    payors_csv = payors_csv[['full_name', 'id_no', 'program_name', 'program_enrollment_event_id', 'plan_name', 'insurance_type', 'policy_num']]
    payors_csv['full_name'] = payors_csv['full_name'].str.strip()
    service_history_csv['full_name'] = service_history_csv['full_name'].str.strip()
    payors_csv = payors_csv.drop(payors_csv[payors_csv.program_name != 'CCBHC'].index)

    merged = service_history_csv.merge(payors_csv, on=['program_enrollment_event_id', 'full_name'])
    merged['service_date'] = pd.to_datetime(merged.service_date)
    merged = merged.drop_duplicates(keep='first', inplace=False)

    merged.to_csv(filename, index=False)


ccbhc_service_history()
