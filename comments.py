import math
# COMMENTS IN PYTHON

# Block Comment: A block comment explains the code that follows it. Typically, you indent a block
# comment at the same level as the code block.

# calculate British Columbia GST/VST taxes on a product that costs 4.99$
priceTaxed = 4.99 * 1.12
print(math.ceil(priceTaxed))

# Inline Comment: When you place a comment on the same line as a statement, you'll have an inline comment
salary = 60000 * 1.02  # increase salary by 2%
print(salary)

# Python docstrings: A documentation string is a string literal that you put as the first lines in a code block
# for example a function

### def quicksort():
  ##  """sort the list using quicksort algorithm """
  #  ...
