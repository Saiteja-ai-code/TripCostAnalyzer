
From = input("From:")
To = input("To:")
type = input("Enter type of vehicle:")
company = input("Enter company of vehicle:")
Mil = float(input("Enter the mileage of vechicle:"))
distance = int(input("how many kms:"))
Toll = int(input("Enter the no.of Tolls:"))
toll_cost = int(input("Enter the per Toll cost:"))
others = int(input("Others cost:"))
fuel_price = float(input("Enter present fuel price:"))
person= int(input("Enter how many members"))
rent_choice = int(input("Rent car? 1.Yes 2.No"))
match rent_choice:
    case 1:
        rent = float(input("Enter the rent"))
    case _:
        print("own vechicle")

#calcutation
fuel_required = distance / Mil
toll_cost = toll_cost * Toll
total_fuel_cost = fuel_required * fuel_price
total_cost = total_fuel_cost + toll_cost + others + rent
per_person = total_cost / person


#output
print("------------DEATILES-------------")
print("From:",From)
print("To",To)
print("vehicle type:",type)
print("vechicle company",company)
print("Mileage of the vechicle:",Mil)
print("Distance",distance,"kms")
print("No of tolls:",Toll)
print("per toll cost:",toll_cost)
print("Other costs:",others)
print("fuel per liter:",fuel_price)
print(person,"menbers")

print("--------------FINAL RESULT-------------")
print("fuel requried:",fuel_required,"liters")
print("toll cost:",toll_cost)
print("fuel cost:",total_fuel_cost)
print("total cost:",total_cost)
print("per person:",per_person)
