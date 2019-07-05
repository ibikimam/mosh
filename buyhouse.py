""" good_credit = False
bad_credit = True
house_cost = 1000000

if good_credit:
    print("house down payment will be", int(house_cost)*0.1 )
else:
    print("house down payment will be", int(house_cost)*.2) 
print("thank you")        """
house_cost = 1000000
good_credit = True
if good_credit:
    downpayment = 0.1 * house_cost

else:
    downpayment = 0.2 * house_cost

print(f'Downpayment = ${downpayment}')        