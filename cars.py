cars=['audi','chevrolet','citroen','renault','ford','Ferrari','bmw','vw',]
print(cars)
for car in cars:
    if car=='bmw' or car=='vw':
        print(car.upper())
    else:
        print(car.title())
if cars[5]=='ferrari': #spelling does not match the list.
    print('Matches')
else:
    print('Does not match')
if cars[5]=='Ferrari': #spelling matches the list.
    print('Matches')
else:
    print('Does not match')
#in these examples we are able to see how the spelling of a variable is 
# relevant in Pythoin as it is case sensitive.
if (cars[5].lower())=='ferrari': #spelling does not match the list.
    print('Matches')
else:
    print('Does not match')
#in this last if statement we modified the initial value to lower case so when 
# compared to the input it does match.

print(cars)