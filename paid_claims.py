from datetime import date, timedelta
import pandas as pd


def paid_claims():
    filename = "C:/Users/mingus/Documents/" + str((date.today().replace(day=1) - timedelta(days=1)).month) + "-" + str(
        (date.today().replace(day=1) - timedelta(days=1)).year) + '_paid_claims.csv'
    df = pd.read_csv('C:/Users/mingus/Documents/paid_claims.csv')
    df = df[['invoice_number', 'submit_number', 'claim_type', 'claim_type_desc', 'receiver', 'is_self_pay', 'is_claim',
             'is_held', 'claim_held_reason', 'claim_held_reason_code', 'claim_held_reason2', 'claim_held_reason_code2',
             'payor_name', 'plan_name', 'is_in_contract', 'policy_num', 'service_date', 'duration',
             'total_service_time', 'units', 'rate_name', 'gl_amount', 'agency_amount', 'amount_charged',
             'amount_expected', 'amount_paid', 'copay_amount', 'other_deductions', 'total_amount_paid',
             'total_write_off', 'status_date', 'status_entered', 'reference_number', 'action_code', 'claim_status',
             'claim_action', 'is_action_performed', 'has_action_performed', 'billing_staff_credentials', 'is_combined',
             'rate_used', 'plan_rate', 'procedure_name', 'procedure_code', 'modifier1', 'modifier2', 'modifier3',
             'is_rebill', 'original_invoice_id', 'orig_inv_number', 'last_name', 'first_name', 'dob',
             'medicaid_number', 'id_no', 'other_id_number', 'check_no', 'check_amount', 'check_date', 'remittance_no',
             'balance', 'ar_balance', 'ar_submission_balance', 'age_service_date', 'age_billing_date',
             'age_submitted_date', 'rem_amount_paid', 'staff_name', 'staff_license', 'staff_license_code',
             'icd9_code', 'icd10_code', 'description', 'claim_adjustment_reasons_code',
             'claim_adjustment_reasons_description']]
    df['service_date'] = pd.to_datetime(df.service_date)
    df.sort_values(by=['payor_name', 'plan_name', 'service_date', 'last_name'], inplace=True)
    df.to_csv(filename, index=False)


paid_claims()