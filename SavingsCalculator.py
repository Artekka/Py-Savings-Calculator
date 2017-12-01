def calculateSavings():
    print('Please enter how much gross income you expect to make every week:' )
    weeklyIncome = int(input())
    print('Please enter the number of weeks you expect to work:')
    weeks = int(input())
    savings = 0
    annualIncome = float(weeklyIncome * weeks)
    userTaxBracket = findTaxBracket(annualIncome)
    taxedAmount = weeklyIncome * userTaxBracket
    netIncome = weeklyIncome - taxedAmount
    print("What percentage (%) of your income would you like to save each week?")
    wishToSave = int(input())
    savedPercent = float(wishToSave / 100)
    print("You have chosen to save: " + str(float(wishToSave)) + "%")
    print("Your net income per week is: ${:,}".format(int(netIncome)))
    print("Your tax bracket is: {:.1f}%".format(userTaxBracket * 100))
    x = 0
    for x in range(1, weeks+1):
        savings += float(netIncome)*savedPercent
    netIncome *= weeks
    print("In {0} weeks you will have saved ${1:,} from ${2:,}.".format(str(x),int(savings),int(netIncome)))
    
def findTaxBracket(income):
  taxBrackets = [(418400, 0.396), (416700, 0.35), (191650, 0.33), (91900, 0.28), (37950, 0.25), (9325, 0.15), (0, 0.10)] 
  return [tax for (tax_limits, tax) in taxBrackets if income > tax_limits][0]

def taxableIncome(taxBracket, income):
  taxes = [
    (0.396, income - (121505.25 + (0.396 * (418400 - 121505.25)))),
    (0.35, income - 120910.25 + (0.35 * (416700 - 120910.25))),
    (0.33, income - 46643.75 + (0.33 * (191650 - 46643.75))),
    (0.28, income - 18713.75 + (0.28 * (91900 - 18713.75))),
    (0.25, income - 5226.25 + (0.25 *(37950 - 5226.25))),
    (0.15, income - 932.50 + (0.15 * (9325 - 932.50))),
    (0.10, income - 0)
    ]

  return 

calculateSavings()
