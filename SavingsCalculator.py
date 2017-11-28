def calculateSavings():
    print('Please enter how much gross income you expect to make every week:' )
    weeklyIncome = int(input())
    print('Please enter the number of weeks you expect to work:')
    weeks = int(input())
    savings = 0
    taxBracket = float(weeklyIncome * weeks)
    if (taxBracket > 418400): taxBracket = 0.396
    elif (taxBracket >= 416700): taxBracket = 0.35
    elif (taxBracket >= 191650): taxBracket = 0.33
    elif (taxBracket >= 91900): taxBracket = 0.28
    elif (taxBracket >= 37950): taxBracket = 0.25
    elif (taxBracket >= 9325): taxBracket = 0.15
    else: taxBracket = 0.10
    taxedAmount = weeklyIncome * taxBracket
    netIncome = weeklyIncome - taxedAmount
    print("What percentage (%) of your income would you like to save each week?")
    wishToSave = int(input())
    savedPercent = float(wishToSave / 100)
    print("You have chosen to save: " + str(float(wishToSave)) + "%")
    print("Your net income per week is: $" + str(int(netIncome)))
    print("Your tax bracket is: " + str(float(taxBracket)*100) + "%")
    for x in range(1, weeks+1):
        savings += float(netIncome)*savedPercent
    netIncome *= weeks
    print("In {0} weeks, you have saved ${1} from ${2}.".format(str(x),str(int(savings)), str(int(netIncome))))
calculateSavings()
