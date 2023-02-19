text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# create an empty list to store the split text of words then
# use the .split method to store it into the split text
split_text = []

for char in text:
    split_text = text.split()
print(split_text)

# create an intersection of the set of words with the prepositions
# set provided above
preps_used = prepositions.intersection(split_text)

# finally print the intersection to see the results
print(preps_used)
