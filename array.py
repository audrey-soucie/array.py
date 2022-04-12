# array.py
print('Audrey Soucie')

cars = ['Ford' ,'Chrysler' ,'Dodge' ,'Ram' ,'Jeep' ,'Chevy', 'GMC']
print(cars)

print('The size of cars array is: ', len(cars))

cars.append('Buick')
print(cars)

print (cars[3])

cars[4] = 'Toyota'
print(cars)

cars.pop(6)
print(cars)

cars.sort(reverse=True)
print(cars)

#16 - Create a variable called my_array_length with a value of the cars array length (spelling, capitilization, and spaces matter)
my_array_length = len(cars)

#17 - create a variable called array_string with a value of 'The length of my array is '
array_string = "The length of my array is "

print (array_string, my_array_length)