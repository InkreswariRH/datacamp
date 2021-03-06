# Once again, we've loaded the credit card records of our four suspects into a DataFrame called credit_records.
# Let's examine the items that they've purchased.

# The pandas module has been imported under the alias pd.
# The DataFrame credit_records has already been imported.


# precode, data
import pandas as pd
credit_records = pd.read_csv('credit_records.csv')


# Instruction 1/2
# Select the column item from credit_records using brackets and string notation.

# Select the column item from credit_records
# Use brackets and string notation
items = credit_records["item"]

# Display the results
print(items)


# Instruction 2/2
# Select the column item from credit_records using dot notation.

# Select the column item from credit_records
# Use dot notation
items = credit_records.item

# Display the results
print(items)
