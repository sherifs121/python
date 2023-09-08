# --------------------------------
# --Ternary Conditional Operator---
# ---------------------------------

country = "EGYPT"

if country == "EGYPT":

    print(f"the weather in {country} is 15")

elif country == "KSA":

    print(f"The Whether in {country} is 30")

else:

    print("country is Not in The List")

# short If

movieRate = 18
age = 16

if age < movieRate:

    print("Movie S Not Good 4U")  # Condition if true

else:

    print("Movie S Good 4U And Happy Watching ")  # Condition if False
print("move s not good 4u" if age < movieRate else "Movie S Good 4U Happy Watching")

# Condition If True  | If Condition | Else | Condition If False
