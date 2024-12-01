name_input=input("Please enter your name: ")
age_input=int(input(f"Welcome to Jurassic Park {name_input.title().rstrip()}! please enter your age: "))
if age_input < 4:
    print(f"{name_input.title()} The cost of entry is free!")
elif age_input < 15:
    print(f"{name_input.title()} The cost of entry is $15 + GST!")
elif age_input <= 60:
    print(f"{name_input.title()} The cost of entry is $30 + GST")
else:
    print(f"{name_input.title()} The cost of entry is $25 + GST")