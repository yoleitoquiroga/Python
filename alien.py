alien_0={'color': 'green', 'points': 5}
for index, value in enumerate(alien_0):
    print(f'Index{index}: {value}')

#accessing the different pairs in the dictionary
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)
#adding akey-value pairs to an already existing dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print(f'The alien is {alien_0["color"]}.')#The alien is green.
alien_0['color'] = 'yellow'
print(f'The alien is now {alien_0["color"]}.')#The alien is now yellow.

alien_position={'x_position' : 0, 'y_position' : 25, 'speed' : 'fast'}
print(f'Original position: {alien_position["x_position"]}')
#miovng alien to the right.
#determine ow far to move the alien based on its current speed.
if alien_position['speed'] =='slow':
    x_increment = 1
elif alien_position['speed'] == 'medium':
    x_increment = 2
else:
    #this mustbe a fast alien
    x_increment = 3

#the new position is the old position plus the increment 
alien_position['x_position'] = alien_position['x_position'] + x_increment
print(f'New position: {alien_position["x_position"]}')

#removing a key-value pair from a dictionary
print(alien_0) #dictionary is whole
del alien_0['points'] #'points' key-value pair deleted fom alien_0 dictionary
print(alien_0)

name=alien_0.get('name', 'No "name" value assigned.')
print(name)