from datetime import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd


def program_referrals():
    filename = "C:/Users/mingus/Documents/" + str(dt.now().month) + "-" + str(dt.now().year) + "_program_referrals.xlsx"

    xl_writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    df = pd.read_csv('C:/Users/mingus/Documents/program_referrals.csv')

    df.to_excel(xl_writer, sheet_name='Program Referrals', index=False)
    worksheet = xl_writer.sheets['Program Referrals']

    plt.rc('font', size=8)
    figsize = 10.0
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(figsize, figsize))

    df.referral_from.value_counts().plot(kind='pie', label='', ax=ax1)
    df.referral_reason.value_counts().plot(kind='pie', label='', ax=ax2)
    ax1.set_title('Referral From')
    ax2.set_title('Referral Reason')
    fig.tight_layout()
    # fig.subplots_adjust(left=1/figsize, right=1-.5/figsize, bottom=1/figsize, top=1-.5/figsize, wspace=0.7)
    fig.savefig('program_referrals.png')
    worksheet.insert_image('A20', 'program_referrals.png')

    xl_writer.save()


program_referrals()
