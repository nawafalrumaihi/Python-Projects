farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farm_animals)

for animals in farm_animals:
    print(animals)

print()
print("Indexing a sequence")
animals_list = ['cow', 'sheep', 'hen', 'goat', 'horse']
goat = animals_list[3]
print(goat)

# print("Indexing a set is not possible")
# goat = farm_animals[3]

more_animals = {'sheep', 'goat', 'cow', 'horse', 'hen'}

if more_animals == farm_animals:
    print('the sets are equal')
else:
    print('the sets are different')