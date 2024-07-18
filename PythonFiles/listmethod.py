# #popmethod
# my_list = [1, 2, 3, 4]
# removed_element = my_list.pop(1)
# print(my_list)
# print("Removed Element:", removed_element)
# # Output: [1, 3, 4]
# # Removed Element: 2

# #removemethod
# my_list = [1, 2, 3, 2, 4]
# my_list.remove(2)
# print(my_list)
# # Output: [1, 3, 2, 4]

# #insertmethod
# my_list = [1, 2, 3]
# my_list.insert(1, 4)
# print(my_list)
# # Output: [1, 4, 2, 3]

# #xtendmethod
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1)
# # Output: [1, 2, 3, 4, 5, 6]

# #appendmethod
# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)
# # Output: [1, 2, 3, 4]

# # Return the smallest element in the list
# min_value = min(my_list)
# print(min_value)  # Output: 1

# # Return the largest element in the list
# max_value = max(my_list)
# print(max_value)  # Output: 5

# # Return the sum of all elements in the list
# sum_value = sum(my_list)
# print(sum_value)  # Output: 15

# # Return the number of elements in the list
# length = len(my_list)
# print(length)  # Output: 5



# y = ['a', 'b', 'c', 'd']
# y.insert(1,'e')
# print(y)

# # a = {'a', 'b', 'c'}
# # v = list(x)
# # print(v[0])

# # Words={"ApplE", "Banana", "Cup", "Dove"}
# # x=input ("Enter word:")
# # for n in Words:
# #     if n == x:
# #         print("Welldone", " ",x,"is the word you got")
# #         break
# #     else:
# #         print('The word' '',x,"is not available")
# #         break

# my_alphabets = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
# spelling = input('Enter spelling: ')
# for x in spelling:
#     if x in my_alphabets:
#         print(x.upper(),x)
#     else:
#         print('Not found')


# x = ("a", "b","c","d","e")
# thistuple = ("a", "b","c","d","e")
# y = list(thistuple)
# y.extend(("f","g"))
# thistuple = tuple(y)
# print(thistuple)

# Newname = input("Enter name: ")
# Name = ("ujunwa", "professor","elliot", "mojjam")

# if type(Name) == list:
#     Name[1] = Newname
#     print(Name)
# elif type(Name) == tuple:
#     print("Not changeable")
# else:
#     print("None of the above")

Item1 = {"name":"Mojjam", "Age": 32, "Address": "Lagos"}
Item2 = {"name":"professor", "Age": 42, "Address": "Ibadan"}
Item3 = {"name":"Ujunwa", "Age": 52, "Address": "Delta"}
Names = [Item1, Item2, Item3]

x = "My name is", Item1.get("name"), "and i am", Item1.get("Age"), "years old."
print()

# for index, x in enumerate(Names, start=1):
#         print(f'{index}{x}')
