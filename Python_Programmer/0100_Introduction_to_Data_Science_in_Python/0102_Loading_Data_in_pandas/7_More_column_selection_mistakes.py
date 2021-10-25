# Another junior detective is examining a DataFrame of Missing Puppy Reports.
# He's made some mistakes that cause the code to fail.

# The pandas module has been loaded under the alias pd, and the DataFrame is called mpr.

# precode, data
import pandas as pd
mpr = pd.read_csv('mpr.csv')

# Instruction 1/3
# Inspect the DataFrame mpr using info().

# Use info() to inspect mpr
print(mpr.info())


# Instruction 2/3
# Correct the mistakes in the code so that it runs without errors.

# The following code contains one or more errors
# Correct the mistakes in the code so that it runs without errors

# Select column "Dog Name" from mpr
name = mpr["Dog Name"]

# Select column "Missing?" from mpr
is_missing = mpr["Missing?"]

# Display the columns
print(name)
print(is_missing)


# Instruction 3/3
# Question
# Why did this code generate an error?
# name = mpr.Dog Name


# Possible Answers

# We need to remove the space in Dog Name.
# If a column name has capital letters, then it needs to be in brackets and string notation.
# * If a column name contains a space, then it needs to be in brackets and string notation.
