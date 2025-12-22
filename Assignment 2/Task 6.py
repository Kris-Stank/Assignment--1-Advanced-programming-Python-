def all_eq(list_of_strings):
    max_length = max(len(s) for s in list_of_strings)   
    for i in range(len(list_of_strings)):
        difference = max_length - len(list_of_strings[i])
        list_of_strings[i] += ("_" * difference)
    
    return list_of_strings

list_of_strings = input().split()
result = all_eq(list_of_strings)
print(result)

# # def all_eq(lst):
#     return [s + "_" * (max(len(x) for x in lst) - len(s)) for s in lst]
