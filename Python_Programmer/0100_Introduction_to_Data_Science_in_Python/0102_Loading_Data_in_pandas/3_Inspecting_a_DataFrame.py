# We've loaded the credit card records of our four suspects into a DataFrame called credit_records.
# Let's learn more about the structure of this DataFrame.

# The pandas module has been imported under the alias pd.
# The DataFrame credit_records has already been imported.

# How many rows are in credit_records?

# precode, data
import pandas as pd
credit_records = pd.read_csv('credit_records.csv')

# Instruction 1/2
# Use the .info() method to inspect the DataFrame credit_records

# Use .info() to inspect the DataFrame credit_records
print(credit_records.info())


# Instruction 2/2

# Question
# How many rows are in credit_records?

# Possible Answers
# 103
# * 104
# 5
# 64
