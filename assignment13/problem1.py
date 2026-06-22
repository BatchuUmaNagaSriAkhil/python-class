#Secret Message Decoder
s = input()

freq = {}

# Count frequency of each character
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

values = list(freq.values())

valid = False

for f in set(values):
    temp = values[:]
    temp.remove(f)

    if len(set(temp)) == 1 or len(temp) == 0:
        valid = True
        break

# Check if already valid
if len(set(values)) == 1:
    valid = True

print("YES" if valid else "NO")