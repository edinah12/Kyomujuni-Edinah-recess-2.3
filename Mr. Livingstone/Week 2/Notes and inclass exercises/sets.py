#sets
my_set = {1, 2, 3, 4, 5}
print(my_set)
my_set.add(6)
print(my_set)
my_set.update([7, 8, 9])
print(my_set)
 
a=[1,2,3,4,5]
print(type(a))

Food= ["posho","beans","cassava"]
print(Food)
print(type(Food))

#ACCESSING AN ITEM IN A LIST
print(Food[0])  # Access the first item
print(Food[1])  #Access the second item
print(Food[-1])  # Access the last item

#use of a constractor to create a list
Food_list = list(("posho", "beans", "cassava"))

#adding an item to the list
Food_list.append("rice")
print(Food_list)

#add an item at a specific position
Food_list.insert(1, "matoke")
print(Food_list)

#update an item in a list
Food_list[2] = "maize"
print(Food_list)

#iterating through lists using loops
for item in Food_list:
    print(item)