#definning dictionries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
#nesting dictionaries into a list
aliens = [alien_0, alien_1, alien_2]
print(aliens)
for item in aliens:
    print(item)

#creating a list of 30 aliens

aliens_group = [] #begin with an empty list.
#making 30 aliens.
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'} #all 30 aliens 
    #have the same key-value elements in this case.
    aliens_group.append(new_alien) #alliens are appended to the initial empty list.
#show the first 5 aliens
for alien in aliens_group[:5]: #second argument tells Python to show the first 5 elements.
    print(alien)
print('...')

#show how many aliens have been created.
print(f'\n\tTotal number of aliens: {len(aliens_group)}')

