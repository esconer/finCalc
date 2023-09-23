from npv import *


def pi(cashflow, discount_rate, r=4):
    """
    use optional argument r to make your answer precise(default is 4), r represent the round off precision which is how many numbers you want after the decimal point

    """
    p_values = pv(cashflow, discount_rate)
    inflow = []
    outflow = []
    for i in p_values:
        if i > 0:
            inflow.append(i)
        else:
            outflow.append(i)
    # print(inflow)
    # print(outflow)
    # print(list_sum(inflow))
    # print(-list_sum(outflow))
    pi = round(list_sum(inflow) / -list_sum(outflow), r)

    # # alternative way
    # np_value=npv(cashflow,discount_rate,r)
    # pi=(np_value/-cashflow[0])+1

    return pi
