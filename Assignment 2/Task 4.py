text_length, word_length = input().split()
text= input()
countr = 0

unique_words = []
for i in range(int(text_length)-int(word_length)+1):
    piece = text[i:i+int(word_length)]
    if piece not in unique_words:
        unique_words.append(text[i:i+int(word_length)])
        countr += 1

print(countr)