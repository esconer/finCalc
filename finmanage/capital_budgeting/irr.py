from npv import *

# cashflow=[24000,8000,4000,20000]
# initial=44000


def irr(cashflow, initial):
    alt_k = 0
    alt_npv = npv(cashflow, initial, alt_k)

    npv_list = []
    while alt_npv:
        alt_k += 1
        # print(alt_k)
        # print(alt_npv)
        new_npv = round(npv(cashflow, initial, alt_k), 4)
        npv_list.append(new_npv)
        alt_npv = new_npv
        if alt_npv < 0:
            break
    surplus = npv_list[-2]
    deficit = npv_list[-1]
    # print(alt_k-1)
    # print((surplus/(surplus-deficit)))
    irr = round((alt_k - 1) + (surplus / (surplus - deficit)), 4)
    # print(surplus,deficit)
    return irr


# irr(cashflow,initial)
