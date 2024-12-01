for value in range(1,6):
    print(value)

#using the list() function to crete a list generated with range()

numbers=list(range(1,11))
print(numbers)
for index, element in enumerate(numbers):
    print(f'Index {index}: Number {element}')

#implementing third argument "step"

increase=list(range(0,21,2))
print(increase) #increasing list by 2
decrease=list(range(20,-1,-2))
print(decrease) #decresing list by 2

#generating a list of the square numbers from 0 to 10
squares=[] #first step is to create an empty list.
for value in range(0, 11): #second, stating the range of numbers we want to work with.

    #square=value**2 #create a variable for each iteration of the for loop and elevate it square.
    
    squares.append(value**2) #append the squared variable to the original empty list.
print(squares) #print the list of squares.

#list comprehensions

squares=[value**2 for value in range(1,11)]
print (f'comprehension {squares}'.title())
#simple statistics with a lsit of numbers
digits=list(range(0, 21))
print(digits)
_min=min(digits)
_max=max(digits)
_sum=sum(digits)
print(_min, _max, _sum)