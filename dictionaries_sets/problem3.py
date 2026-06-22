'''
Group anagram:
i/p:["eat","tea","tan","ate","ant","nat","bat","tab]
o/p:[[eat,tea,ate],[tan,nat,ant],[bat,tab]]


'''
words =["eat", "tea", "tan", "ate","ant", "nat","bat","tab"]

anagrams = {}

for i in range(len(words)):
    j = "".join(sorted(words[i]))

    if j not in anagrams:
        anagrams[j] = []

    anagrams[j].append(words[i])

result = list(anagrams.values())

print(result)