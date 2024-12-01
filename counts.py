#counting to twenty
for number in list(range(0, 21)):
    print(number)

#one million
million=list(range(0, 1000001))
#for num in million:
    #print (num)

#summing a million 
_min=min(million)
_max=max(million)
_sum=sum(million)
print(_min, _max, _sum)

#odd numbers
for number in list(range(1,21,2)):
    print(number)

#miltiples of 3
threes=list(range(3,31,3))
print(threes)
for number in threes:
    print(number)

#cubes
cubes=[]
for number in range(1,11):
    cubes.append(number**3)
print(cubes)

#cube comprehension
_cubes=[number**3 for number in range(1,11)]
print(_cubes)