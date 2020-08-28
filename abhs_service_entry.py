from datetime import datetime as dt
import pandas as pd


def abhs_service_entry():
    report_bruns = pd.read_csv('C:/Users/mingus/Documents/report_bruns.csv')
    report_moffett = pd.read_csv('C:/Users/mingus/Documents/report_moffett.csv')
    report_bruns = report_bruns[['full_name', 'id_no', 'program_name', 'event_name', 'staff_name', 'duration',
                                 'actual_date', 'date_entered']]
    report_moffett = report_moffett[['full_name', 'id_no', 'program_name', 'event_name', 'staff_name', 'duration',
                                     'actual_date', 'date_entered']]
    report_bruns['actual_date'] = pd.to_datetime(report_bruns.actual_date)
    report_bruns['date_entered'] = pd.to_datetime(report_bruns.date_entered)
    report_moffett['actual_date'] = pd.to_datetime(report_moffett.actual_date)
    report_moffett['date_entered'] = pd.to_datetime(report_moffett.date_entered)

    report_bruns['date_diff'] = report_bruns['date_entered'] - report_bruns['actual_date']
    report_moffett['date_diff'] = report_moffett['date_entered'] - report_moffett['actual_date']

    report_bruns.sort_values(by=['staff_name', 'actual_date'], inplace=True)
    report_moffett.sort_values(by=['staff_name', 'actual_date'], inplace=True)

    xl_writer_bruns = pd.ExcelWriter('C:/Users/mingus/Documents/report_bruns.xlsx', engine='xlsxwriter')
    xl_writer_moffett = pd.ExcelWriter('C:/Users/mingus/Documents/report_moffett.xlsx', engine='xlsxwriter')

    report_bruns.to_excel(xl_writer_bruns, sheet_name='Bruns', index=False)
    report_moffett.to_excel(xl_writer_moffett, sheet_name='Moffett', index=False)
    workbook_bruns = xl_writer_bruns.book
    workbook_moffett = xl_writer_moffett.book
    worksheet_bruns = xl_writer_bruns.sheets['Bruns']
    worksheet_moffett = xl_writer_moffett.sheets['Moffett']

    red_format_bruns = workbook_bruns.add_format({'bg_color': '#FF4C4C',
                                             'font_color': '#9C0006'})
    yellow_format_bruns = workbook_bruns.add_format({'bg_color':   '#FFEB9C',
                                               'font_color': '#9C6500'})
    green_format_bruns = workbook_bruns.add_format({'bg_color':   '#C6EFCE',
                                                    'font_color': '#006100'})
    worksheet_bruns.conditional_format('I2:I'+str(len(report_bruns)+1), {'type': 'cell',
                                                                  'criteria': '>',
                                                                  'value': 3.5,
                                                                  'format': red_format_bruns})
    worksheet_bruns.conditional_format('I2:I' + str(len(report_bruns)+1), {'type': 'cell',
                                                                         'criteria': 'between',
                                                                         'minimum': 1.5,
                                                                         'maximum': 3.5,
                                                                         'format': yellow_format_bruns})
    worksheet_bruns.conditional_format('I2:I' + str(len(report_bruns)+1), {'type': 'cell',
                                                                         'criteria': '<',
                                                                         'value': 1.5,
                                                                         'format': green_format_bruns})

    red_format_moffett = workbook_moffett.add_format({'bg_color': '#FF4C4C',
                                                  'font_color': '#9C0006'})
    yellow_format_moffett = workbook_moffett.add_format({'bg_color': '#FFEB9C',
                                                     'font_color': '#9C6500'})
    green_format_moffett = workbook_moffett.add_format({'bg_color': '#C6EFCE',
                                                    'font_color': '#006100'})
    worksheet_moffett.conditional_format('I2:I' + str(len(report_moffett) + 1), {'type': 'cell',
                                                                             'criteria': '>',
                                                                             'value': 3.5,
                                                                             'format': red_format_moffett})
    worksheet_moffett.conditional_format('I2:I' + str(len(report_moffett) + 1), {'type': 'cell',
                                                                             'criteria': 'between',
                                                                             'minimum': 1.5,
                                                                             'maximum': 3.5,
                                                                             'format': yellow_format_moffett})
    worksheet_moffett.conditional_format('I2:I' + str(len(report_moffett) + 1), {'type': 'cell',
                                                                             'criteria': '<',
                                                                             'value': 1.5,
                                                                             'format': green_format_moffett})

    xl_writer_bruns.save()
    xl_writer_moffett.save()


abhs_service_entry()
