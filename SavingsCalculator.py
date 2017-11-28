def calculateSavings():
    print('Please enter how much gross income you expect to make every week:' )
    weeklyIncome = int(input())
    print('Please enter the number of weeks you expect to work:')
    weeks = int(input())
    savings = 0
    annualIncome = float(weeklyIncome * weeks)
    taxBrackets = [(418400, 0.396), (416700, 0.35), (191650, 0.33), (91900, 0.28), (37950, 0.25), (9325, 0.15), (0, 0.10)] 
    def determine_taxBracket(income):
      return [tax for (tax_limits, tax) in taxBrackets if income > tax_limits][0]
    user_taxBracket = determine_taxBracket(annualIncome)
    taxedAmount = weeklyIncome * user_taxBracket
    netIncome = weeklyIncome - taxedAmount
    print("What percentage (%) of your income would you like to save each week?")
    wishToSave = int(input())
    savedPercent = float(wishToSave / 100)
    print("You have chosen to save: " + str(float(wishToSave)) + "%")
    print("Your net income per week is: $" + str(int(netIncome)))
    print("Your tax bracket is: " + str(float(user_taxBracket)*100) + "%")
    x = 0
    for x in range(1, weeks+1):
        savings += float(netIncome)*savedPercent
    netIncome *= weeks
    print("In {0} weeks, you have saved ${1} from ${2}.".format(str(x),str(int(savings)), str(int(netIncome))))
calculateSavings()
