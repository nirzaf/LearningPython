print ('Hello World')
x  = 10

#get the square of x
y = x**2
print (y)

#create a list of animals
animals = ['cat', 'dog', 'rabbit']
print(animals[1])

animals[2] = 'turtle'
print(animals)

del animals[2] 
print(animals)

#create a list of vehicles with 10 elements
vehicles = ['car', 'motorbike', 'truck', 'van', 'bus', 'lorry', 'train', 'bicycle', 'jeep', 'ship']

vehicles.append('airplane')
print(vehicles)

#sort the vehicle list
vehicles.sort()
print(vehicles)

vehicles.reverse()
print(vehicles)

#return the length of the list
print(len(vehicles))

#print all vehicle names in for loop
for x in vehicles:
    print(x)

#print all numbers from 1 to 10
for x in range(1,11):
    print(x)

#create a list of numbers with 10 elements
numbers = [1,2,3,4,5,6,7,8,9,10]

#print min value from numbers
print(min(numbers))

#print max value from numbers
print(max(numbers))

#print sum of all numbers from numbers
print(sum(numbers))

#create a list of operating systems
OS = ['Windows', 'Mac', 'Linux', 'Android', 'iOS']

#slicing the list 
print(OS[1:3])

#using for loop with slice list
for OS in OS[1:4]:
    print(OS)

#Copying lists using slicing lists

#create a list of programming languages 
languages = ['Python', 'Java', 'C++', 'C#', 'PHP', 'JavaScript']
progLang = languages[2:4]

print(progLang)

progLang.append('Golang')
print(progLang)

#Tuples in python
tup = (200,500,1000,2000,5000,10000)
print(tup)
print(tup[2])
print(tup[-1])

#To do for loop with tuples
for tup in tup:
    print(tup)

#To do overwriting with tuples
tup = (200,500,1000,2000)
print(tup)

