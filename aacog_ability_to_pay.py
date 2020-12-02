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


def main():
    income = float(input('Enter monthly income: ').strip())
    size = int(input('Enter family size: ').strip())
    print(max_monthly_fee(income, size))


main()
