admin_names=['leonardo','roberto','pilar','cecilia','carmen','andres','jose']   
name_input=input("Please enter your namne: ")
age_input=int(input("Please enter your age: "))
if name_input.lower() in admin_names and age_input >= 18:
    print(f'Welcome back {name_input.title()}.')
else:
    print(f'I am sorry {name_input.title()}, you are not allowed entry.')