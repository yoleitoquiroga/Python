current_number = 0 #Start with a value lower than the comparison (10).
while current_number < 10: #Current number compared to.
    current_number += 1 #Increasing current_number by 1 each time.
    if current_number % 2 == 0: #If reminder of division is 0, even number.
        continue #Loops back to the while loop.
    
    print(current_number) #once reminder is not 0, odd number this one is printed.