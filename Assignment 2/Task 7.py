# Shopping List Analysis
from collections import Counter

items = input().split()
freq = Counter(items)

print("Purchase frequency:")
for item, count in freq.items():
    print(f"{item}: {count}")

print("Most popular item:", freq.most_common(1)[0][0])

print("Purchased once:",
      " ".join(item for item, count in freq.items() if count == 1))

print("Sorted by frequency:")
for item, count in freq.most_common():
    print(item, count)
