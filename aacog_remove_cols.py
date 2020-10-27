import pandas as pd
from tkinter import messagebox, filedialog as fd
from xlsxwriter.exceptions import FileCreateError


def main():
    filename = fd.askopenfilename(title='Select the report file that needs column removal')
    report = pd.read_excel(filename)
    report = report[['invoice_number', 'claim_held_reason', 'payer_name_output', 'service_date', 'units',
                     'amount_charged', 'amount_paid', 'procedure_name', 'procedure_code', 'modifier1', 'last_name',
                     'first_name', 'middle_name', 'medicaid_number', 'id_no', 'check_no', 'check_amount', 'check_date',
                     'program_unit_code', 'program_unit', 'icd10_code', 'description']]
    report.to_excel(filename, index=False)


while True:
    try:
        main()
    except FileCreateError:
        messagebox.showerror('Error', 'Cannot edit file while it is open. Please close the file and try again.')
        continue
    except KeyError:
        messagebox.showerror('Error', 'One of the columns specified for deletion does not exist. Please ensure you '
                                      'have selected the correct file and try again. If the error persists, please '
                                      'contact Eli Anderson at eanderson@khitconsulting.com')
        continue
    except FileNotFoundError:
        messagebox.showerror('Error', 'File does not exist.')
        quit()
    except Exception as e:
        messagebox.showerror('Fatal Error', 'An unexpected error has occurred. Please contact Eli Anderson at '
                                            'eanderson@khitconsulting.com and include this error message: ' + str(e)
                             )
        quit()
    break
messagebox.showinfo('Success', 'Columns successfully deleted!')



