#lists define how data is stored and organized in a program. They are a collection of
#  items that can be of any data type, including numbers, strings, and even other lists. 
# Lists are defined using square brackets [] and can be modified by adding,
#  removing, or changing elements.

#what makes a list unique is that it can hold multiple values of different data types, 
# and the values can be accessed using their index position in the list.

#python's simplest data structure is a list, which is a collection of items that can 
# be of any data type, including numbers, strings, and even other lists. Lists are defined 
# using square brackets [] and can be modified by adding, removing, or changing elements.   

#lists are dynamis in size and can increase or decrease in size as needed.
#  They can also be nested, meaning that a list can contain other lists as elements.

#lists can hold different datat types but often you do not want to mix data types in a list,
#  as it can make it more difficult to work with the data.

#lists are mutable, meaning that their elements can be changed after they are created.
#to create a list, we can use the following syntax:

#my_list = [item1, item2, item3]

#you can initialize a list with any number of items, including zero items. For example,
#  to create an empty list, we can use the following syntax:

#my_list = []  # creates an empty list

#lists can be indexed and sliced, meaning that we can access individual elements or
#  subsets of the list using their index positions. The first element in a list has an

names = []
test_scores =[100, 95, 90, 85, 80]

#to modify or add elements to a list, we hae to know its index position. For example,
#  to change the first element in a list, we can use the following syntax:
#the index in python starts at 0, so the first element in a list has an index of 0, 
# the second element has an index of 1, and so on.

#print(test_scores[0])  # prints the first element in the list, which is 10
#we can also add data using the append() method, which adds an element to the
#  end of the list. For example,

names.append("John")  # adds "John" to the end of the list
names.append("Jane")  # adds "Jane" to the end of the list
names.append("Jim")  # adds "Jim" to the end of the list

print(names)  # prints the list of names, which is ["John", "Jane", "Jim"]

# one of the biggest advantages of using lists is the ability to loop, search and 
# process data in a list. For example, we can use a for loop to iterate over the 
# elements in a list and perform operations on them.

#count the number of items in a list using for loop
#count = 0
#for item in test_scores:
    #count += 1
#print(f"Number of items in the list: {count}")

#looking for = 90
#found = False   

#.index function can return the index position of an item in a list.
#  If the item is not found, it will raise a ValueError.

print(names.index("Jane"))  # prints the index position of "Jane", which is 1