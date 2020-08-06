from datetime import datetime as dt
import pandas as pd

def join_datatables():
    tp_csv = pd.read_csv("C:/Users/mingus/Documents/treatment_due_dates.csv")
    pw_csv = pd.read_csv("C:/Users/mingus/Documents/primary_workers.csv")

    tp_csv['name'] = tp_csv['name'].str.strip()
    pw_csv['name'] = pw_csv['name'].str.strip()

    merged = tp_csv.merge(pw_csv, on='name')
    merged.drop(['people_id', 'id_no', 'ssn_number', 'ssi_number', 'urn_no', 'dob',
                 'phone_day', 'phone_evening', 'aka', 'intake_date', 'discharge_date',
                 'client_status', 'ipd', 'service_track_id', 'gender', 'medicaid_number',
                 'current_location', 'program_enrollment_event_id', 'program_info_id',
                 'worker_assignment_id', 'worker_start', 'worker_end', 'staff_id',
                 'supervisor_id', 'supervisor_name_y', 'is_primary_worker', 'managing_office_id',
                 'managing_office', 'worker_number', 'unit_number', 'worker_unit', 'prg_days',
                 'last_date_serv', 'total_dist', 'grand_total_dist', 'worker_role', 'program_name'], axis=1, inplace=True)
    merged = merged.rename(columns = {'worker_name':'primary_worker'})
    merged['expiration_date'] = pd.to_datetime(merged.expiration_date)
    merged.sort_values(by=['primary_worker', 'expiration_date'], inplace=True, ascending=[True, True])
    merged.to_csv("C:/Users/mingus/Documents/" + str(dt.now().month+1) + "-" + str(dt.now().year) +
                  "_treatment_plan_due_dates.csv", index=False)

join_datatables()
