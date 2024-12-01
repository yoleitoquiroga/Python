cars=['chevrolet', 'audi', 'ford', 'ferrari', 'bmw', 'saab', 'citroen', 'lada','mercedes benz'] 
print(cars)
print(cars[0].title())
print(cars[0].upper())
print(cars[1])
print(cars[3])
print(cars[5])
print(cars[-1])

#using lists in a f-string
message=f'My first car was a {cars[0].title()} but currently I really want a {cars[-1].title()}'
print(message)

#len() shows the amount of elements in a list
number_of_elements=len(cars)
print(f'this list contains {number_of_elements} elements')

#the use of the function enumerate() shows us the diffferent elements in a list and when coded with the for looop it can display the index to its respective element from the list 

for index, element in enumerate(cars):
    print(f"Index {index}: {element}")

#modifying elements in a list. 1) identify the list that needs to be updated, 2)identify the index of the element that needs to be changed, 3)assign a new value to it.


for index, element in enumerate(cars):
    print(f"Index {index}: {element}") #running this loop after modifying the list shows the item changed in index 5.

#appending elements to a list

cars.append('bentley') # bentley has been added to the end of the list
print(cars)
for index, element in enumerate(cars): #index list displays the latest addition to the original list
    print(f'Index {index}: {element}')

# inserting elements to the list

cars.insert(7, 'volvo') #in this example, volvo will take the index number 7 and the rest of the list will shift one space to the right.
print(cars)
for index, element in enumerate(cars):
    print(f'Index {index}: {element}')

names=[] #empty list is created
names.insert(0, 'leonardo') #new elements are added to the list with their respective index.
names.insert(1, 'oscar')
names.insert(2, 'mauricio')
names.insert(3, 'camilo')
names.insert(4, 'daniel')
print(names)
number_of_names=len(names)
print(f'this list contains {number_of_names} for now')
names.insert(3, 'juan')
for index, element in enumerate(names):
    print(f'Index {index}: {element}')

#removing elements with the del statement
del cars [5] #in this example, saab has been removed permanently from the list
print(cars)
for index, element in enumerate(cars):
    print(f'Index {index}: {element}')


#removing elements with the pop() method

removed_names=names.pop(5) #in this example the name under the index no. 5 has been removed from the names list and saved in the removed_names list
print(names)
for index, element in enumerate(names):
    print(f'Index {index}: {element}')
print(f'The following member has been removed: {removed_names}')# removed_names list showing the popped element.**

#removing elements with the remove() method
gone_names='mauricio' #the specified element has been stored in the gone_names list
names.remove(gone_names) #the specified element in gone_names is removed from the names list
for index, element in enumerate(names):
    print(f'Index {index}: {element}')
print(f'{gone_names} is no longer with us!\n')

#organizing a list with the sort() method

print(cars) #original order of list
cars.sort() 
print(cars)# list organized in alphabetical order
cars.sort(reverse=True)
print(f'{cars}\n') #list organized in reverse alpabetical order
#once the order of a list is changed with the sort() method, it cannot be reversed to its original order.

#organizing a list with the sorted() function

print(names) #original order of the list.
print(sorted(names)) #list organized alphabetically.
print(sorted(names, reverse=True)) #list organized in reverse alphabetical order.
print(f'names\n') #list printed back again in its original order.

#organizing a list in reverse order by using the reverse() method

print(names) #list in its original order.
names.reverse()
print(names) #list in reverse order.
print(len(names)) #to be displayed remember to include the len() function inside the print() function
for index, element in enumerate(names):
    print(f'Index {index}: {element}')