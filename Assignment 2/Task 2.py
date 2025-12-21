a_mainstring, b_substring = input(), input()

substring_list = []
for i in range(len(b_substring)):
    if (b_substring[i:] + b_substring[:i]) not in substring_list:
        substring_list.append(b_substring[i:] + b_substring[:i])

countr = 0

for i in range(len(a_mainstring) - len(b_substring) + 1):
    piece = a_mainstring[i:i+len(b_substring)]
    if piece in substring_list:
        countr += 1

print(countr)