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