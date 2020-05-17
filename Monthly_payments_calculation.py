import argparse
import os
import numpy as np

os.system("clear")

parser = argparse.ArgumentParser()
parser.add_argument('--capital', type=float, default=500000, help="The capital asked from the bank")
parser.add_argument('--year', type=int, default=25, help="The number of years to repay the loan")
parser.add_argument('--tax', type=float, default=1000, help="The annual taxes of the house")
parser.add_argument('--charges', type=float, default=3000, help="The annual charges of the house")
parser.add_argument('--additional_charges', type=float, default=500, help="Additional charges (food, transportation, gym, etc..)")
parser.add_argument('--salary', type=float, default=2000, help="monthly salary plus incomes")
args = parser.parse_args()


C = args.capital
n = args.year
charges_yearly = args.charges
charges_perso = args.additional_charges
taxes = args.tax 
salary = args.salary

total_charges = charges_yearly + taxes


interest_rates = np.arange(1,3,0.1)/100 # from 1% 'til 3%, change as you wish 
for t in list(interest_rates) : 

    m  = (C*t/12)/(1-(1+t/12)**(-12*n))

    # Output
    print("Interest rate : {0:.2f}%".format(t*100))
    print("Monthly payment : {0:.2f}".format(m))
    print("Monthly payements + charges : {0:.2f}".format(m + total_charges/12))
    print("What's left each month : {0:.2f}".format(salary-(m+total_charges/12) - charges_perso))
    print("Cost of the credit (interests) : {0:.2f}".format(m*12*n-C))
    print("Cost of the credit (capital + interests) {0:.2f}".format(m*12*n))
    print("*"*50)    
