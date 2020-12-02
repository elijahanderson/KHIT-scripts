from tkinter import *
from tkinter import messagebox


def max_monthly_fee(income, size):
    if income < 1595.0:
        return 0
    elif 1595 <= income < 1782:
        if size == 1:
            return 40
        elif size > 1:
            return 0
    elif 1782 <= income < 1968:
        if size == 1:
            return 47
        elif size > 1:
            return 0
    elif 1968 <= income < 2155:
        if size == 1:
            return 56
        elif size > 1:
            return 0
    elif 2155 <= income < 2342:
        if size == 1:
            return 64
        elif size == 2:
            return 40
    elif 2342 <= income < 2528:
        if size == 1:
            return 74
        elif size == 2:
            return 47
        elif size > 2:
            return 0
    elif 2528 <= income < 2715:
        if size == 1:
            return 83
        elif size == 2:
            return 56
        elif size > 2:
            return 0
    elif 2715 <= income < 2902:
        if size == 1:
            return 94
        elif size == 2:
            return 64
        elif size == 3:
            return 40
        elif size > 3:
            return 0
    elif 2902 <= income < 3088:
        if size == 1:
            return 105
        elif size == 2:
            return 74
        elif size == 3:
            return 47
        elif size > 3:
            return 0
    elif 3088 <= income < 3275:
        if size == 1:
            return 117
        elif size == 2:
            return 83
        elif size == 3:
            return 56
        elif size > 3:
            return 0
    elif 3275 <= income < 3462:
        if size == 1:
            return 129
        elif size == 2:
            return 94
        elif size == 3:
            return 64
        elif size == 4:
            return 40
        elif size > 4:
            return 0
    elif 3462 <= income < 3648:
        if size == 1:
            return 142
        elif size == 2:
            return 105
        elif size == 3:
            return 74
        elif size == 4:
            return 47
        elif size > 4:
            return 0
    elif 3648 <= income < 3835:
        if size == 1:
            return 155
        elif size == 2:
            return 117
        elif size == 3:
            return 83
        elif size == 4:
            return 56
        elif size > 4:
            return 0
    elif 3835 <= income < 4022:
        if size == 1:
            return 170
        elif size == 2:
            return 129
        elif size == 3:
            return 94
        elif size == 4:
            return 64
        elif size == 5:
            return 40
        elif size > 5:
            return 0
    elif 4022 <= income < 4208:
        if size == 1:
            return 184
        elif size == 2:
            return 142
        elif size == 3:
            return 105
        elif size == 4:
            return 74
        elif size == 5:
            return 47
        elif size > 5:
            return 0
    elif 4208 <= income < 4395:
        if size == 1:
            return 199
        elif size == 2:
            return 155
        elif size == 3:
            return 117
        elif size == 4:
            return 83
        elif size == 5:
            return 56
        elif size > 5:
            return 0
    elif 4395 <= income < 4582:
        if size == 1:
            return 215
        elif size == 2:
            return 170
        elif size == 3:
            return 129
        elif size == 4:
            return 94
        elif size == 5:
            return 64
        elif size == 6:
            return 40
        elif size > 6:
            return 0
    elif 4582 <= income < 4768:
        if size == 1:
            return 232
        elif size == 2:
            return 184
        elif size == 3:
            return 142
        elif size == 4:
            return 105
        elif size == 5:
            return 74
        elif size == 6:
            return 47
        elif size > 6:
            return 0
    elif 4768 <= income < 4955:
        if size == 1:
            return 249
        elif size == 2:
            return 199
        elif size == 3:
            return 155
        elif size == 4:
            return 117
        elif size == 5:
            return 83
        elif size == 6:
            return 56
        elif size > 6:
            return 0
    elif 4955 <= income < 5142:
        if size == 1:
            return 267
        elif size == 2:
            return 215
        elif size == 3:
            return 170
        elif size == 4:
            return 129
        elif size == 5:
            return 94
        elif size == 6:
            return 64
        elif size == 7:
            return 40
        elif size > 7:
            return 0
    elif 5142 <= income < 5328:
        if size == 1:
            return 285
        elif size == 2:
            return 232
        elif size == 3:
            return 184
        elif size == 4:
            return 142
        elif size == 5:
            return 105
        elif size == 6:
            return 74
        elif size == 7:
            return 47
        elif size > 7:
            return 0
    elif 5328 <= income < 5515:
        if size == 1:
            return 304
        elif size == 2:
            return 249
        elif size == 3:
            return 199
        elif size == 4:
            return 155
        elif size == 5:
            return 117
        elif size == 6:
            return 83
        elif size == 7:
            return 56
        elif size > 7:
            return 0
    elif 5515 <= income < 5702:
        if size == 1:
            return 323
        elif size == 2:
            return 267
        elif size == 3:
            return 215
        elif size == 4:
            return 170
        elif size == 5:
            return 129
        elif size == 6:
            return 94
        elif size == 7:
            return 64
        elif size == 8:
            return 40
        elif size > 8:
            return 0
    elif 5702 <= income < 5888:
        if size == 1:
            return 343
        elif size == 2:
            return 285
        elif size == 3:
            return 232
        elif size == 4:
            return 184
        elif size == 5:
            return 142
        elif size == 6:
            return 105
        elif size == 7:
            return 74
        elif size == 8:
            return 47
        elif size > 8:
            return 0
    elif 5888 <= income < 6075:
        if size == 1:
            return 364
        elif size == 2:
            return 304
        elif size == 3:
            return 249
        elif size == 4:
            return 199
        elif size == 5:
            return 155
        elif size == 6:
            return 117
        elif size == 7:
            return 83
        elif size == 8:
            return 56
        elif size > 8:
            return 0
    elif 6075 <= income < 6262:
        if size == 1:
            return 385
        elif size == 2:
            return 323
        elif size == 3:
            return 267
        elif size == 4:
            return 215
        elif size == 5:
            return 170
        elif size == 6:
            return 129
        elif size == 7:
            return 94
        elif size == 8:
            return 64
        elif size >= 9:
            return 40
    elif 6262 <= income < 6448:
        if size == 1:
            return 407
        elif size == 2:
            return 343
        elif size == 3:
            return 285
        elif size == 4:
            return 232
        elif size == 5:
            return 184
        elif size == 6:
            return 142
        elif size == 7:
            return 105
        elif size == 8:
            return 74
        elif size >= 9:
            return 47
    elif 6448 <= income < 6635:
        if size == 1:
            return 429
        elif size == 2:
            return 364
        elif size == 3:
            return 304
        elif size == 4:
            return 249
        elif size == 5:
            return 199
        elif size == 6:
            return 155
        elif size == 7:
            return 117
        elif size == 8:
            return 83
        elif size >= 9:
            return 56
    elif 6635 <= income < 6822:
        if size == 1:
            return 453
        elif size == 2:
            return 385
        elif size == 3:
            return 323
        elif size == 4:
            return 267
        elif size == 5:
            return 215
        elif size == 6:
            return 170
        elif size == 7:
            return 129
        elif size == 8:
            return 94
        elif size >= 9:
            return 64
    elif 6822 <= income < 7008:
        if size == 1:
            return 476
        elif size == 2:
            return 407
        elif size == 3:
            return 343
        elif size == 4:
            return 385
        elif size == 5:
            return 232
        elif size == 6:
            return 184
        elif size == 7:
            return 142
        elif size == 8:
            return 105
        elif size >= 9:
            return 74
    elif 7008 <= income < 7195:
        if size == 1:
            return 500
        elif size == 2:
            return 429
        elif size == 3:
            return 364
        elif size == 4:
            return 304
        elif size == 5:
            return 249
        elif size == 6:
            return 199
        elif size == 7:
            return 155
        elif size == 8:
            return 117
        elif size >= 9:
            return 83
    elif 7195 <= income < 7382:
        if size == 1:
            return 525
        elif size == 2:
            return 453
        elif size == 3:
            return 385
        elif size == 4:
            return 323
        elif size == 5:
            return 267
        elif size == 6:
            return 215
        elif size == 7:
            return 170
        elif size == 8:
            return 129
        elif size >= 9:
            return 94
    elif 7382 <= income < 7568:
        if size == 1:
            return 551
        elif size == 2:
            return 476
        elif size == 3:
            return 407
        elif size == 4:
            return 343
        elif size == 5:
            return 285
        elif size == 6:
            return 232
        elif size == 7:
            return 184
        elif size == 8:
            return 142
        elif size >= 9:
            return 105
    elif 7568 <= income < 7755:
        if size == 1:
            return 577
        elif size == 2:
            return 500
        elif size == 3:
            return 429
        elif size == 4:
            return 364
        elif size == 5:
            return 304
        elif size == 6:
            return 249
        elif size == 7:
            return 199
        elif size == 8:
            return 155
        elif size >= 9:
            return 117
    elif 7755 <= income < 7942:
        if size == 1:
            return 603
        elif size == 2:
            return 525
        elif size == 3:
            return 453
        elif size == 4:
            return 385
        elif size == 5:
            return 323
        elif size == 6:
            return 267
        elif size == 7:
            return 215
        elif size == 8:
            return 170
        elif size >= 9:
            return 129
    elif 7942 <= income < 8128:
        if size == 1:
            return 631
        elif size == 2:
            return 551
        elif size == 3:
            return 476
        elif size == 4:
            return 407
        elif size == 5:
            return 343
        elif size == 6:
            return 285
        elif size == 7:
            return 232
        elif size == 8:
            return 184
        elif size >= 9:
            return 142
    elif 8128 <= income < 8315:
        if size == 1:
            return 658
        elif size == 2:
            return 577
        elif size == 3:
            return 500
        elif size == 4:
            return 429
        elif size == 5:
            return 364
        elif size == 6:
            return 304
        elif size == 7:
            return 249
        elif size == 8:
            return 199
        elif size >= 9:
            return 155
    elif 8315 <= income < 8502:
        if size == 1:
            return 687
        elif size == 2:
            return 603
        elif size == 3:
            return 525
        elif size == 4:
            return 453
        elif size == 5:
            return 385
        elif size == 6:
            return 323
        elif size == 7:
            return 267
        elif size == 8:
            return 215
        elif size >= 9:
            return 170
    elif 8502 <= income < 8688:
        if size == 1:
            return 716
        elif size == 2:
            return 631
        elif size == 3:
            return 551
        elif size == 4:
            return 476
        elif size == 5:
            return 407
        elif size == 6:
            return 343
        elif size == 7:
            return 285
        elif size == 8:
            return 232
        elif size >= 9:
            return 184
    elif 8688 <= income < 8875:
        if size == 1:
            return 745
        elif size == 2:
            return 658
        elif size == 3:
            return 577
        elif size == 4:
            return 500
        elif size == 5:
            return 429
        elif size == 6:
            return 364
        elif size == 7:
            return 304
        elif size == 8:
            return 249
        elif size >= 9:
            return 199
    elif 8875 <= income < 9062:
        if size == 1:
            return 776
        elif size == 2:
            return 687
        elif size == 3:
            return 603
        elif size == 4:
            return 525
        elif size == 5:
            return 453
        elif size == 6:
            return 385
        elif size == 7:
            return 323
        elif size == 8:
            return 267
        elif size >= 9:
            return 215
    elif 9062 <= income < 9248:
        if size == 1:
            return 806
        elif size == 2:
            return 716
        elif size == 3:
            return 631
        elif size == 4:
            return 551
        elif size == 5:
            return 476
        elif size == 6:
            return 407
        elif size == 7:
            return 343
        elif size == 8:
            return 285
        elif size >= 9:
            return 232
    elif 9248 <= income < 9435:
        if size == 1:
            return 838
        elif size == 2:
            return 745
        elif size == 3:
            return 658
        elif size == 4:
            return 577
        elif size == 5:
            return 500
        elif size == 6:
            return 429
        elif size == 7:
            return 364
        elif size == 8:
            return 304
        elif size >= 9:
            return 249
    elif 9435 <= income < 9622:
        if size == 1:
            return 870
        elif size == 2:
            return 776
        elif size == 3:
            return 687
        elif size == 4:
            return 603
        elif size == 5:
            return 525
        elif size == 6:
            return 453
        elif size == 7:
            return 385
        elif size == 8:
            return 323
        elif size >= 9:
            return 267
    elif 9622 <= income < 9808:
        if size == 1:
            return 903
        elif size == 2:
            return 806
        elif size == 3:
            return 716
        elif size == 4:
            return 631
        elif size == 5:
            return 551
        elif size == 6:
            return 476
        elif size == 7:
            return 407
        elif size == 8:
            return 343
        elif size >= 9:
            return 285
    elif 9808 <= income < 9995:
        if size == 1:
            return 936
        elif size == 2:
            return 838
        elif size == 3:
            return 745
        elif size == 4:
            return 658
        elif size == 5:
            return 577
        elif size == 6:
            return 500
        elif size == 7:
            return 429
        elif size == 8:
            return 364
        elif size >= 9:
            return 304
    elif 9995 <= income < 10182:
        if size == 1:
            return 970
        elif size == 2:
            return 870
        elif size == 3:
            return 776
        elif size == 4:
            return 687
        elif size == 5:
            return 603
        elif size == 6:
            return 525
        elif size == 7:
            return 453
        elif size == 8:
            return 385
        elif size >= 9:
            return 323
    elif 10182 <= income < 10368:
        if size == 1:
            return 1004
        elif size == 2:
            return 903
        elif size == 3:
            return 806
        elif size == 4:
            return 716
        elif size == 5:
            return 631
        elif size == 6:
            return 551
        elif size == 7:
            return 476
        elif size == 8:
            return 407
        elif size >= 9:
            return 343
    elif 10368 <= income < 10555:
        if size == 1:
            return 1039
        elif size == 2:
            return 936
        elif size == 3:
            return 838
        elif size == 4:
            return 745
        elif size == 5:
            return 658
        elif size == 6:
            return 577
        elif size == 7:
            return 500
        elif size == 8:
            return 429
        elif size >= 9:
            return 364
    elif 10555 <= income < 10742:
        if size == 1:
            return 1074
        elif size == 2:
            return 970
        elif size == 3:
            return 870
        elif size == 4:
            return 776
        elif size == 5:
            return 687
        elif size == 6:
            return 603
        elif size == 7:
            return 525
        elif size == 8:
            return 453
        elif size >= 9:
            return 385
    elif 10742 <= income < 10928:
        if size == 1:
            return 1111
        elif size == 2:
            return 1004
        elif size == 3:
            return 903
        elif size == 4:
            return 806
        elif size == 5:
            return 716
        elif size == 6:
            return 631
        elif size == 7:
            return 551
        elif size == 8:
            return 476
        elif size >= 9:
            return 407
    elif 10928 <= income < 11115:
        if size == 1:
            return 1147
        elif size == 2:
            return 1039
        elif size == 3:
            return 936
        elif size == 4:
            return 838
        elif size == 5:
            return 745
        elif size == 6:
            return 658
        elif size == 7:
            return 577
        elif size == 8:
            return 500
        elif size >= 9:
            return 429
    elif 11115 <= income < 11302:
        if size == 1:
            return 1185
        elif size == 2:
            return 1074
        elif size == 3:
            return 970
        elif size == 4:
            return 870
        elif size == 5:
            return 776
        elif size == 6:
            return 687
        elif size == 7:
            return 603
        elif size == 8:
            return 525
        elif size >= 9:
            return 453
    elif 11302 <= income < 11488:
        if size == 1:
            return 1223
        elif size == 2:
            return 1111
        elif size == 3:
            return 1004
        elif size == 4:
            return 903
        elif size == 5:
            return 806
        elif size == 6:
            return 716
        elif size == 7:
            return 631
        elif size == 8:
            return 551
        elif size >= 9:
            return 476
    elif 11488 <= income < 11675:
        if size == 1:
            return 1261
        elif size == 2:
            return 1147
        elif size == 3:
            return 1039
        elif size == 4:
            return 936
        elif size == 5:
            return 838
        elif size == 6:
            return 745
        elif size == 7:
            return 658
        elif size == 8:
            return 577
        elif size >= 9:
            return 500
    elif 11675 <= income < 11862:
        if size == 1:
            return 1301
        elif size == 2:
            return 1185
        elif size == 3:
            return 1074
        elif size == 4:
            return 970
        elif size == 5:
            return 870
        elif size == 6:
            return 776
        elif size == 7:
            return 687
        elif size == 8:
            return 603
        elif size >= 9:
            return 525
    elif income >= 11862:
        if size == 1:
            return 1340
        elif size == 2:
            return 1223
        elif size == 3:
            return 1111
        elif size == 4:
            return 1004
        elif size == 5:
            return 903
        elif size == 6:
            return 806
        elif size == 7:
            return 716
        elif size == 8:
            return 631
        elif size >= 9:
            return 551


def main():
    def retrieve():
        income = float(income_entry.get().strip())
        size = int(float(size_entry.get().strip()))  # convert to float first to avoid ValueError exception
        if income <= 0 or size <= 0:
            disp['text'] = 'Enter positive non-zero integers only'
        else:
            disp['text'] = 'The maximum monthly fee is $%s' % str(max_monthly_fee(income, size))

    root = Tk()
    root.title('Monthly Ability-To-Pay Fee')
    root.geometry('400x200')

    income_label = Label(root, font='Helvetica 12', text='Monthly Gross Income: ')
    income_label.grid(row=0, column=0)
    income_entry = Entry(root, bd=1, font='Helvetica 12')
    income_entry.grid(row=0, column=2, pady=10)

    size_label = Label(root, font='Helvetica 12', text='Household Family Size: ')
    size_label.grid(row=4, column=0)
    size_entry = Entry(root, bd=1, font='Helvetica 12')
    size_entry.grid(row=4, column=2, pady=10)

    submit = Button(root, text='Submit', font='Helvetica 12', command=retrieve)
    submit.place(relx=0.5, rely=0.85, anchor=CENTER)
    root.bind('<Return>', lambda event=None: submit.invoke())

    disp = Label(root, font='Helvetica 14 bold',
                 text='The maximum monthly fee is...')
    disp.place(relx=0.5, rely=0.6, anchor=CENTER)

    root.mainloop()


while True:
    if __name__ == '__main__':
        try:
            main()
        except Exception as e:
            messagebox.showerror('Fatal Error', 'An unexpected error has occurred. Please contact Eli Anderson at '
                                                'eanderson@khitconsulting.com and include this error message: ' + str(e)
                                 )
            quit()
        break
