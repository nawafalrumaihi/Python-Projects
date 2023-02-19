favourites = {'door screen',
              'frying pan',
              'roller blind',
              'football',
              'coffee grinder',
              'bush hat',
              'stirling engine',
              'cachemira cd',
              'shirt',
              }

basket = {'garlic crusher',
          'stirling engine',
          'frying pan',
          'shirt',
          'bush hat',
          }

# create an empty list called suggestions that will store the sorted list of
# the customer's favourite items `without` any items that are in their basket
suggestions = favourites.difference(basket)
print(sorted(suggestions))
