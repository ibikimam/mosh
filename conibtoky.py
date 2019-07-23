""" weight = input('please type your weight \n')
w = int(weight)
unit = input('please select (L)Lbs or (K)Kg \n')
u = unit
if u == "l" or "L":
    total_weight= w*0.45
    print(f"your weight in Kgs is {total_weight}Kg")

elif u == "k" or "K":
     total_weight= w*(1/0.45)
     print(f"your weight in pounds is {total_weight}lbs")"""

weight=int(input('Please type in your weight\n'))
unit = input('please select (L)Lbs or (K)Kg \n')

if unit.upper() == "L":
    total_weight= weight * 0.45
    print(f"your weight in Kgs is {total_weight} Kg")
else:
    total_weight= weight / e0.45
    print(f"your weight in pounds is {total_weight} lbs")        

