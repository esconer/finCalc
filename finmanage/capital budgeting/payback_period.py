# pay back period = initial investment / annual cash inflow
# where annual cash inflow = profit after tax + depreciation
#where profit after tax = profit before tax - tax  or profit before tax(1- tax rate)


#situation 1: uniform cashflow throughout the years
# one project
def uniform_cashflow():
   initial = int(input("what is your initial investment?\n--> "))
   profit_b_tax= int(input("what is your profit before excluding tax?\n--> "))
   dep=int(input('what is your annual depreciation?\n'))
   tax_rate= int(input('what is the tax rate?\n (e.g. 40 it will mean 40%)\n--> '))
   profit_a_tax= profit_b_tax*(1-(tax_rate/100))
   annual_cashinflow=profit_a_tax-dep
   payback_period= round(initial/annual_cashinflow,2)
   print(f"your initial investment will be recovered within {payback_period} years")



def non_uniformcashflow():
   initial = int(input("what is your initial investment?\n--> "))
   dep=int(input('what is your annual depreciation?\n'))
   tax_rate= int(input('what is the tax rate?\n (e.g. 40 it will mean 40%)\n--> '))
   years =int(input("How many years of cash flows?\n"))
   profit_b_tax= []
   profit_a_tax=[]
   annual_cashinflow=[]
   cumulative_cashinflow=[]
   for i in range(years):
      p_b_tax = int(input(f"what is your profit before excluding tax of {i + 1} year?: "))  
      profit_b_tax.append(p_b_tax) 
      pat= round(profit_b_tax[i]*(1-(tax_rate/100)))
      profit_a_tax.append(pat)
      annual_inflow=round(profit_a_tax[i]-dep)
      annual_cashinflow.append(annual_inflow)
      if (len(annual_cashinflow)==1):
         
         cumulative_cashinflow.append(annual_cashinflow[i])
      else:
         # print("annual_cashinflow",annual_cashinflow[i],annual_cashinflow[i-1])
         c_inflow=cumulative_cashinflow[i-1] + annual_cashinflow[i]
         # print("cumulative_cashinflow",cumulative_cashinflow)
         # print("c_inflow",c_inflow)
         cumulative_cashinflow.append(c_inflow)
         # print("after cumulative",cumulative_cashinflow)

   for i in cumulative_cashinflow:
    if i > initial :
        pv_year= cumulative_cashinflow.index(i)
        print(pv_year)
        part_of_another_year= round(((i-initial)/cumulative_cashinflow[pv_year-1])*365)
        payback_period = f"{pv_year}years {part_of_another_year}days"
        print("your payback period is ",payback_period)

# years =int(input("How many years of cash flows?\n"))
# cashflows =[]
# for i in range(years):
#    cashflow = float(input(f"Cash flow of year {i + 1}: "))  
#    cashflows.append(cashflow) 

def main():
   is_uniform_cashflow= input("Do you have a uniform cashflow form the project?\n type 'y' if Yes type 'n' if No\n-->")
   if is_uniform_cashflow=="y":
      uniform_cashflow()
   else:
      non_uniformcashflow()
      
main()