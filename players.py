players=['gabriela','patricia','nicole','sofia','maria','thalia','camila','mariana','laura','marcela','tatiana','valentina','pilar','madison']
for index, value in enumerate(players):
    print(f'Index {index}: {value}'.title()) #personally i find this for loop helpful when it comes down to figuring out the index of the different elements in a list.
print(f'{players[2:]}'.title()) #if you ommit the second index in a slice, python replaces it with the end of the list
print(f'{players[2:5]}'.title())
print(f'{players[:4]}'.title())#same goes for ommiting the first index, python replaces it wih the begginning of the list.

#using a for loop in a slice

print('A mi me gusta mucho la: ')
for name in (players[:4]):
    print(name)

#copying a list

my_foods=['salmon','rice','vegetables','croisants','yogurt'] #original list.
friend_foods=my_foods[:] #original list copied to create an exact replica under another list name

print(f'My favourite foods are: \n{my_foods}\n')
print(f"My friend's favourite foods are: \n{friend_foods}\n")

my_foods.append('tomatoes') #tomatoes will be added to the end of the my_foods list
friend_foods.append('pumpkin') #pumpkin will be added to the end of the list of the friend_foods list
#THE ADDITION OF THESE NEW VALUES WILL NOT BE REFLECTED IN BOTH LISTS SIMULTANEOUSLY BUT IN EACH INDEPENDENT ONE.

print(f'My favourite foods are: \n{my_foods}\n')
print(f"My friend's favourite foods are: \n{friend_foods}\n")

print("The first three items in the players list are:")
for element in players[:3]:
    print(f'{element}'.title())

print("\nThree items in the middle of the players list are:")
for element in players[5:8]:
    print(f'{element}'.title())

print("\nThe last three items in the players list are:")
for element in players[-3:]:
    print(f'{element}'.title())

print(len(players))

pizzas = [
    "Margherita Pizza",
    "Pepperoni Pizza",
    "Hawaiian Pizza",
    "Meat Lovers Pizza",
    "Vegetarian Pizza",
]
#"BBQ Chicken Pizza",
 #   "Supreme Pizza",
   # "White Pizza",
   # "Buffalo Chicken Pizza",
   # "Pesto Pizza"

friend_pizzas=pizzas[:]
pizzas.append('Chicken Pizza')
friend_pizzas.append('Supreme Pizza')
print('\nMy favourite pizzas are:')
for element in pizzas:
    print(element)

print("\nMy friend's favourite pizzas are:")
for element in friend_pizzas:
    print(element)