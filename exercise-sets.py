# Create a set of things that bite, or things that sting:
# Spiders bite, scorpions and vespas sting.
# Spiders and scorpions are arachnids, so you can also
# get a set of arachnids by forming the union of those two sets

# list of sets
scorpions = {"emperor", "red claw", "arizona", "forest", "fat tail"}
snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
spiders = {"tarantula", "black widow", "wolf spider", "crab spider"}
vespas = {"yellowjacket", "hornet", "paper wasp"}

# since spiders bite and also they're the only one group, we can just print the set
print("-" * 120)
print(f"These types of spiders bite:\n{spiders}")
print("-" * 120)

# adding scorpions and vespas to the animal sting set using the union operator:
print("-" * 120)
animals_that_sting = scorpions | vespas
print(f"These animals can sting:\n{animals_that_sting}")
print("-" * 120)

# adding spiders and scorpions for the arachnids set using the union operator
print("-" * 120)
arachnids_species = scorpions | spiders
print(f"These animals are arachnids:\n{arachnids_species}")
print("-" * 120)
