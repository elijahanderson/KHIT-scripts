from datetime import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd


def program_referrals():
    filename = "C:/Users/mingus/Documents/" + str(dt.now().month) + "-" + str(dt.now().year) + "_program_referrals.xlsx"

    xl_writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    df = pd.read_csv('C:/Users/mingus/Documents/program_referrals.csv')

    df.to_excel(xl_writer, sheet_name='Program Referrals', index=False)
    worksheet = xl_writer.sheets['Program Referrals']

    # df.referral_from.value_counts().plot(kind='pie', label='', ax=ax1)
    # df.referral_reason.value_counts().plot(kind='pie', label='', ax=ax2)
    # ax1.set_title('Referral From')
    # ax2.set_title('Referral Reason')
    # fig.tight_layout()
    # fig.savefig('program_referrals.png')
    # worksheet.insert_image('A20', 'program_referrals.png')

    xl_writer.save()


def test():
    filename = "C:/Users/mingus/Documents/" + str(dt.now().month) + "-" + str(dt.now().year) + "_program_referrals.xlsx"

    df = pd.read_csv('C:/Users/mingus/Documents/program_referrals.csv')
    df.to_csv(filename)


program_referrals()
