# pay back period = initial investment / annual cash inflow
# where annual cash inflow = profit after tax + depreciation
#where profit after tax = profit before tax - tax  or profit before tax(1- tax rate)

# one project

initial = int(input("what is your initial investment?\n--> "))
profit_b_tax= int(input("what is your profit before excluding tax?\n--> "))
dep=int(input('what is your annual depreciation?\n'))
tax_rate= int(input('what is the tax rate?\n (e.g. 40 it will mean 40%)\n--> '))
profit_a_tax= profit_b_tax*(1-(tax_rate/100))
annual_cashinflow=profit_a_tax-dep
payback_period= round(initial/annual_cashinflow,2)
print(f"your initial investment will be recovered within {payback_period} years")
