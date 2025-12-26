text = input()
words = text.split()

result_words = []
w = 0
while w < len(words):
    word = words[w]

    letters = []
    i = 0
    while i < len(word):
        letters.append(word[i])
        i += 1

    i = 0
    while i < len(letters):
        j = 0
        while j < len(letters) - 1:
            if letters[j] > letters[j + 1]:
                tmp = letters[j]
                letters[j] = letters[j + 1]
                letters[j + 1] = tmp
            j += 1
        i += 1

    new_word = ""
    i = 0
    while i < len(letters):
        new_word += letters[i]
        i += 1

    result_words.append(new_word)
    w += 1

out = ""
i = 0
while i < len(result_words):
    if i > 0:
        out += " "
    out += result_words[i]
    i += 1

print(out)
