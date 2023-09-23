def pv_factor_gen(discount_rate, years, r=4):
    """
    use optional argument r to make your answer precise(default is 4), r represent the round off precision which is how many numbers you want after the decimal point
    """
    pv_factor = []

    for i in range(years):
        factor = 1 / pow((1 + (discount_rate / 100)), i)
        pv_factor.append(round(factor, r))
        # print(pv_factor)
    return pv_factor


def pv(cashflow, discount_rate, r=4):
    years = len(cashflow)

    pv_factor = pv_factor_gen(discount_rate, years, r)
    p_value = []
    # pv_factor =pv_factor_gen(k)
    for i in range(len(cashflow)):
        # print(cashflow[i])
        # print(pv_factor[i])
        single_pv = cashflow[i] * pv_factor[i]
        p_value.append(round(single_pv, r))
    # print(p_value)
    return p_value


def list_sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum


def npv(cashflow, discount_rate, r=4):
    p_value = pv(cashflow, discount_rate, r)
    npv = list_sum(p_value)

    return round(npv, r)
