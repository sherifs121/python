# -----------------
# --control flow--
# --if, elif , else--
# --make decitions--
# -----------------
uName = "Sherif"
isStudent = "Yes"
uCountry = "KSA"
cName = "Python Course"
cPrice = 100
cDiscount = 30
if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar":    
  
    if isStudent == "Yes":
        print(f"Hello{uName}\'Because You Arw From : {uCountry} And student")
        print(f"Hello {uName} The Course \"{cName}\"Price Is: ${cPrice - 90}")
    else:
        print(f"Hello{uName}\'Because You Arw From : {uCountry}")
        print(f"Hello {uName} The Course \"{cName}\"Price Is: ${cPrice - 80}")
elif uCountry == "Kuwait" or uCountry == "Bahrain":
    
    print(f"Hello{uName} Because You Arw From : {uCountry}")
    print(f"Hello {uName} The Course \"{cName}\"Price Is: ${cPrice - 80}")
else:
    
    print(f"Hello{uName}Because You Arw From{uCountry}")
    print(f"Hello {uName} The Course \"{cName}\"Price Is: ${cPrice - 30}")
