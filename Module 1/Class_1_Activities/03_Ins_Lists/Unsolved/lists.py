# -*- coding: utf-8 -*-
"""Instructor Demo: Lists.

This script showcases basic operations of Python Lists.
"""

# Print every other element
print("Printing every other city")
every_other_city = where_we_live[::2]
print(every_other_city)

# Print the last element of the list
print("The last city is...")
last_city = where_we_live[-1]
print(last_city)


# Change a specified element within the list at the given index
print("Change the first element in the list...")
where_we_live[0] = "Las Vegas, NV"
print(where_we_live)

# Add an element to the end of the list
print("Adding a new place to the end of the list...")
where_we_live.append("Honolulu, HI")
print(where_we_live)

# Add an element to the end of the list
print("Removing a new place to the end of the list...")
where_we_live.remove("Honolulu, HI")
print(where_we_live)

# Remove an element from the list based on the given index
print("Removing 'Orlando, FL' based off of its index")
florida_index = where_we_live.index("Orlando, FL")
where_we_live.pop(florida_index)
print(where_we_live)
print("---------------")

# Calculate the number of elements within the list
print("Calculating the number of places...")
print(len(where_we_live))
print("---------------")