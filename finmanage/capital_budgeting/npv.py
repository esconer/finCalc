
# def pv_factor_gen(k):
#     pv_factor=[]
#     for i in range(len(cashflow)):
        
#         factor=(1/pow((1+(k/100)),i+1))
#         pv_factor.append(factor)
#         # print(pv_factor)
#     return pv_factor

    
# def pv(cashflow,pv_factor):
    
#     p_value=[]
#     # pv_factor =pv_factor_gen(k)
#     for i in range(len(cashflow)):
#         # print(cashflow[i])
#         # print(pv_factor[i])
#         single_pv=cashflow[i]*pv_factor[i]
#         p_value.append(single_pv)
#     # print(p_value)
#     return p_value
# def npv(cashflow,k):
    
#     npv=0
#     pv_factor= pv_factor_gen(k)
#     p_value = pv(cashflow,pv_factor)
#     for i in p_value:
#         npv+=i
#     return npv

def npv(cashflow,initial,k):
    pv=0
    pv_factor=[]
    p_value=[]
    for i in range(len(cashflow)):
        
        factor=round((1/pow((1+(k/100)),i+1)),4)
        pv_factor.append(factor)
        # print(pv_factor)
    # pv_factor =pv_factor_gen(k)
    for i in range(len(cashflow)):
        # print(cashflow[i])
        # print(pv_factor[i])
        single_pv=cashflow[i]*pv_factor[i]
        p_value.append(single_pv)
    for i in p_value:
        pv+=i
    npv=pv-initial
    return npv

        
    




