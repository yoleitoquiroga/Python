number = int(input("\nEnter a number and I will tell you if it is even or odd: "))
if number %2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

#7-1 rental car.
cars =['subaru', 'chevrolet', 'for', 'ferrari', 'kia'] 
make = input("\nPlease enter the make of the car you would like to rent: ").lower().strip()
print(f"let me see if I can find you a {make.title()}...")
if make in cars:
    print(f"\nHOORRAY!\nWe do in fact have a {make.title()} ready for rent.")
else:
    print(f"\nUnfortunately we do not have a {make.title()} for rent at this location.")
    print("These are the available cars for rent: \n")
    for car in cars:
        print(car.title())

#7-2 restaurant seating.
num_guests = int(input("\nHow many people will be sitting at the table tonight: "))
if num_guests >= 8:
    print("Unfortunately you will have to take a seat and wait for a tale to open.")
else:
    print("A table is being cleared for you as we speak.")

#7-3 multiples of 10.
num = int(input("\nPlesae enter a number: "))
if num % 10 == 0:
    print(f"{num} is a multiple of ten!")
else:
    print(f"{num} is not a multiple of ten!")