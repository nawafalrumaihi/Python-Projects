def copy_pasta(data: dict):
    new_data = {}

    for key, value in data.items():
        if isinstance(value, dict):
            new_data[key] = copy_pasta(value)
        elif isinstance(value, list):
            new_data[key] = value.copy()
        else:
            new_data[key] = value
    return new_data


animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

print(id(animals))
print("*" * 10)
print(id(copy_pasta(animals)))

