# Paycheck.py
# simple passing data to and from function

def calcPayCheck(wages):
    fedTaxRate = 0.23
    stateTaxRate = 0.08

    grossPay = wages / 26.0
    fedTax   = grossPay * fedTaxRate
    stateTax = grossPay * stateTaxRate
    netPay   = grossPay - fedTax - stateTax
    netPay   = round(netPay, 2)
    return netPay


mySalary = 58000.00
myPayCheck = calcPayCheck(mySalary)
print('my paycheck is', myPayCheck)

tonysPayCheck = calcPayCheck(72400.00)
print('tonys paycheck is', tonysPayCheck)

sallysPayCheck = calcPayCheck(82900.00)
print ('sally\'s paycheck is', sallysPayCheck)
