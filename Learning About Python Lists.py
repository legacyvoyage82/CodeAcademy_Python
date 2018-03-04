
# A list is another datatype in Python. It has the following structure:
#     NAME_OF_LIST = ["item 0", "item 1", "item 2", "item 3", "item 4"]

# items on the LIST can be called with the following code:
#     NAME_OF_LIST[3] 

#     the "3" in the structure above is called the "index".
#     This will return the 4th item on the list because PYTHON always counts starting from 0

# Example
#%%

zoo_animals = ["pangolin", "cassowary", "sloth","red panda" ]


if len(zoo_animals) > 3:
  print ("The first animal at the zoo is the " + zoo_animals[0])
  print ("The second animal at the zoo is the " + zoo_animals[1])
  print ("The third animal at the zoo is the " + zoo_animals[2])
  print ("The fourth animal at the zoo is the " + zoo_animals[3])


#%%
# Items from a list can be replaced using the following code:

# NAME_OF_LIST[3] = "NEW ITEM NAME"
#EXAMPLE
List_Cities = ["New York", "Shanghai", "Paris", "London", "Washington"]

print("The origional 4th city on the list was "+List_Cities[3])

print("However, after this following code: ")

print("     List_Cities[3] = 'New Orleans'")

List_Cities[3]="New Orleans"

print("Now the value of the newly replaced 4th city on the list is "+List_Cities[3])

#List can be started without items in them. They can be You can 'append' (add to) them via code
#%%
suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("socks")
suitcase.append("ties")
suitcase.append("shirts")

list_length = len(suitcase) # Set this to the length of suitcase

print ("There are %d items in the suitcase." % (list_length))
print (suitcase)


#List Slicing
#when only a portion of the list is needed, we can introduce a new variable and set it to a selection of items from that list
# 
# example 
#%%
letters = ['a', 'b', 'c', 'd', 'e']
slice = letters[1:3]
#notice that when we call items [1:3] we are only returning the second and third items
print (slice)
print (letters)

#Slicing Lists and Strings
# You can slice a string exactly like a list! In fact, you can think of strings as lists of characters: each character is a sequential item in the list, starting from index 0.

print(letters[:3])
print(letters[2:])

#%%
#Maintaining Order
#we can identify the INDEX number of an item by the use of the index code.

animals = ["ant", "bat", "cat"]
print (animals.index("bat"))

#we can also instert items to a list, and specify where in the index the new item will be placed in.

animals.insert(1, "dog")
print (animals)
#%%
#FOR LOOPS
#If you want to do something with every item in the list, you can use a for loop.
my_list = [1,9,3,8,5,7]

for Variable_Name in my_list:
  # Your code here
  print(2*Variable_Name)

#%%
# We can also sort lists using sort.
# Write a for-loop that iterates over start_list and .append()s each number squared (x ** 2) to square_list.Then sort square_list!

start_list = [5, 3, 1, 2, 4]
square_list = []

for Every_Item_In_Start_List in start_list:
    square_list.append(Every_Item_In_Start_List**2)
    square_list.sort()

print (square_list)
