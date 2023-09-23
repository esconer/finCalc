from npv import *


def irr(cashflow, guess=0, r=4):
    """
    This irr function takes two arguments ,cashflow and a guess . In the cash flow you put a list of cashflow including the initial investment in the start of the list for example if you have cash flows like this -->> first year->20000, second year ->30000 ,third year -> 40000 and your initial investment is 60000 so make a list of cashflow like this cashflow=[-60000,20000,30000,40000]
    you can also provide a optional guess argument to make the code run faster
    """
    alt_k = guess
    alt_npv = npv(cashflow, alt_k, r)

    npv_list = []
    while alt_npv:
        alt_k += 1
        # print(alt_k)
        # print(alt_npv)
        new_npv = npv(cashflow, alt_k, r)
        npv_list.append(new_npv)
        alt_npv = new_npv
        if alt_npv < 0:
            break
    surplus = npv_list[-2]
    deficit = npv_list[-1]
    # print(alt_k-1)
    # print((surplus/(surplus-deficit)))
    irr = round((alt_k - 1) + (surplus / (surplus - deficit)), r)
    # print(surplus,deficit)
    return irr
