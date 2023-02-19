from instructor_deepcopy_challenge import my_deepcopy
import copy

original = {
    "Tim": ["Buchalka", ["Programmer", "Teacher"]],
    "J-P": ["Roberts", ["Programmer", "Teacher"]],
}

# utilizing the deep copy method from the copy module
copy_1 = copy.deepcopy(original)

#the function from the instructor deep-copy challenge solution
copy_2 = my_deepcopy(original)

original["Tim"].append("Australia")
original["J-P"].append("UK")

# refers to the second item for the value of `Tim`
original["Tim"][1].append("Cashier")
jp_list = original["J-P"]
jp_list[1].append("Courier")

print(original)
print(copy_1)
print(copy_2)