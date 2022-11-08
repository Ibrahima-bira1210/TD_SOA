from VerifCredid import is_solvable
from homeAppraisal import home_appraisal

print("=============================================================")
print("########### Hello Welcome to Loan Approval App ##############")
print("=============================================================")

name = input("Enter your name: ")
print("---------------------------------")
ssn = int(input("Enter your ssn: "))
print("---------------------------------")

if not is_solvable(ssn):
    print('Sorry Mr %s you are not solvable so your loan is not approved' % name)
else:
    home_price = int(input("Enter your Home price: "))
    print("---------------------------------")
    loan_amount = int(input("Enter your loan Amount: "))
    if not home_appraisal(home_price, loan_amount):
        print('Sorry Mr %s you are solvable but the loan amount is lower than the home price so your loan is not '
              'approved' % name)
    else:
        print('Congrats Mr %s your loan is approved' % name)
