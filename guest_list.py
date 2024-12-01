guest_list=['daniela','maria', 'nicole', 'thalia', 'sofia', 'carlos', 'miguel', 'daniel', 'eduardo']
for name in (guest_list):
    print(f'Welcome my dear {name.capitalize()}! I am so happy you are here tonight.') 
    #since every element in the list is a single word, the use of title() 
    # becomes conflicting, therefore capitalize() is the right choice in this 
    # case. If the elements in the list were more than a single name, the 
    # title() function would be the right choice as it wold capitalize each name
    # and not just the first one as capitalize() does.
cannot_come='sofia'
guest_list.remove(cannot_come) 
print(f'\nUnfortunatety {cannot_come.capitalize()} will not be able to join us tonihgt.')
can_come='carmen'
guest_list.append(can_come)
print(f'Fortunately our very own {can_come.capitalize()} will be taking her place.')
print('\n')
for name in (guest_list):
    print(f'Do not dispair my estimated {name.capitalize()}, the party will start shortly!')
print('\nGuess what! I was able to find a bigger table for us so I will be able to invite some additional bodies to our party!')
print('\n')
guest_list.insert(0, 'oscar')
guest_list.insert(4, 'leider')
guest_list.insert(-1, 'felipe')
for name in (guest_list):
    print(f'{name.capitalize()}, please join me in the bigger table located on the second floor')
print('\nDue to forseen circumstances that were totally under my control, I will only be able to invite two of you tonight')
print('\n')
while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f'I am so sorry my dear {removed_guest.capitalize()} but I will not be able to invite you out for dinner tonight.')
print('\n')
for name in (guest_list):
    print(f'Now that these suckers are gone, {name.capitalize()} you are my absolute favourite, lets get to dinner!')
print('\n')





guest_list2=['daniela macias','maria restrepo', 'nicole rodriguez', 'thalia rowland', 'sofia merlano', 'carlos aguirre', 'miguel cervantez', 'daniel restrepo', 'eduardo aureles']
for name in (guest_list2):
    print(f'Welcome my dear {name.title()}! I am so happy you are here tonight.') 
    #the elements in the list are more than one word each, thus allowing us to use the title() function instead of capitalize()

for index, element in enumerate(guest_list2):
    print(f'Index {index}: {element}'.title())