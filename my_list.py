#an empty list called my_list
my_list = []

#appending the following element to my_list: 10,20,30,40
my_list.extend([10,20,30,40])

#insert the value 15 at the second position of my_list
my_list.insert(1, 15)

#extend my_list with another list: [50,60,70]
my_list.extend([50,60,70])

#removing the last element from my_list
my_list.pop(-1)

#sort my_list in ascending order
my_list.sort()

#find and print the index of the value 30 in my_list
index_30 = my_list.index(30)
print("Index of 30 in my_list:", index_30)