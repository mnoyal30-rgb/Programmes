unit = int(input("Enter the units consumed: "))
bill = 0 

if unit<=100: 
    bill = unit * 5 
else:
    bill = (100*5) + ((unit-100)*7)

bill+=50 # Fixed charge
print("Total Electricity Bill:",bill)
