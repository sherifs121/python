# -----------------------------------
# --- Practical Membership Control --
# -----------------------------------

# List Contains Admins

admin = ["Ahmed", "Osama", "Sameh", "Manal", "Rahma", "Mahmoud", "Enas"]
print(admin.index("Osama"))
admin[1] = "El-zero"
print(admin)

# Login

name = input("Please Type Your Name").strip().capitalize()

# If Name is in Admin 

if name in admin:
    print(f"Hello {name} Welcome Back")

    option = input("Delete Update Your Name ?").strip().capitalize()
    print(option)

    # Update Option

    if option == 'Update' or option == 'U':
        theNewName = input("Your New Name Please").strip().capitalize()
        print(theNewName)
        admin[admin.index(name)] = theNewName
        print("Name updated.")
        print(admin)

    # Delete Option  
    elif option == 'Delete' or option == 'D':
   
        admin.remove(name)
        print("Name Deleted")
        print(admin)
   
    # Wrong Option
    else:
        print("Wrong option")

# Delete Option

else:
        status = input("Not Admin, Add You Y,N?").strip().capitalize()
        if status =="Yes" or status =="Y":
            print("You Have Been Added")
            admin.append(name)
            print(admin)
        else:
            print("You Are Not Added")