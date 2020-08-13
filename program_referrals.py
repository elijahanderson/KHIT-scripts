import matplotlib.pyplot as plt
import pandas as pd


def program_referrals():
    xl_writer = pd.ExcelWriter('C:/Users/mingus/Documents/program_referrals.xlsx', engine='xlsxwriter')
    df = pd.read_csv('C:/Users/mingus/Documents/program_referrals.csv')

    df.to_excel(xl_writer, sheet_name='Program Referrals', index=False)
    worksheet = xl_writer.sheets['Program Referrals']

    df.referral_from.value_counts().plot(kind='pie', label='')
    plt.savefig('referral_from.png')
    worksheet.insert_image('A20', 'referral_from.png')

    df.referral_reason.value_counts().plot(kind='pie', label='')
    plt.savefig('referral_reasons.png')
    worksheet.insert_image('L20', 'referral_reasons.png')

    xl_writer.save()


program_referrals()
