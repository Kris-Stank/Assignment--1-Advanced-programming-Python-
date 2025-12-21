# >>-->   <--<<
# <<<<>>--><--<<--<<>>>-><<<<<

seq = input()
countr = 0

for i in range(len(seq)-4):
    if seq[i:i+5] == ">>-->" or seq[i:i+5] == "<--<<":
        countr += 1

print(countr)
        