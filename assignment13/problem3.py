#Circular Word Chain
n = int(input())

words = []
seen = set()

valid = True

for _ in range(n):
    word = input()

    # Check repeated word
    if word in seen:
        valid = False

    seen.add(word)
    words.append(word)

# Check chain condition
for i in range(n - 1):
    if words[i][-1] != words[i + 1][0]:
        valid = False
        break

print("VALID" if valid else "INVALID")