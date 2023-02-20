data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# plants_filename = "flowers_print.txt"

# # creates a new .txt file with the list of flowers
# with open(plants_filename, "w") as plants:
#     for plant in data:
#         print(plant, file=plants)
#
# # printing data to the console and listing them inside
# # a list (or array)
# new_list = []
# with open(plants_filename) as plants:
#     for plant in plants:
#         new_list.append(plant.rstrip())
#
# print(new_list)

# plants_filename = "flowers_write.txt"
#
# with open(plants_filename, "w") as plants:
#     for plant in data:
#         plants.write(plant)
#
# print(data)
# string_representation = data.__str__()
# print(type(string_representation))

# prints 0 - 9 on a new line
filename = "test_numbers.txt"
with open(filename, "w") as test:
    for i in range(10):
        print(i, file=test)

# prints 0 - 9 on a new line because of "\n" otherwise,
# would print it as 0123456789 -- but must change to str
# first, otherwise, it will not work.
with open(filename, "w") as test:
    for i in range(10):
        test.write(str(i) + "\n")
