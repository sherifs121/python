#-----------------------------------
#--practical Your Age Full Details--
#-----------------------------------

# Input Age 
age =int(input('what\'s Your Age ? ').strip())
print(age)

# Get Age in All Time Units
months =age *12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print('You Lived For')
print(f"{months} Months.")
print(f"{weeks:,} weeks.")
print(f"{days:,} Days.")
print(f"{hours:,} Hours.")
print(f"{minutes:,} minutes.")
print(f"{seconds:,} seconds.")




