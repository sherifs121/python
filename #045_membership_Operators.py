# ----------------------------------
# --Membership Operators -----------
# ----------------------------------
# in 
# not in 
# ----------------------------------

# String

name = "Osama"
print("s" in name)
print("a" in name)
print("A" in name)

print("#" * 50)

# List

friends = ["Ahmed", "Sayed", "Mahmoud"]
print("Osama" in friends)
print("Sayed" in friends)
print("Mahmoud" not in friends)

print("#" * 50)

# using in and with condition

countriesOne = ["Egypt", "KSA", "Kuwait", "Bahrin", "syria"]
countriesOneDiscount = 80

countriesTwo = ["Italy", "USA" ]
countriesTwoDiscount = 50
myCountry = "Egypt"

if myCountry  in countriesOne:
  
    print(f"Hello You Have A Discount Equal To ${countriesOneDiscount}")

elif myCountry in countriesTwo:
  
    print(f"Hello You Have A Discount Equal To ${countriesTwoDiscount}")

else: 
 
    print("You Have No Discount")