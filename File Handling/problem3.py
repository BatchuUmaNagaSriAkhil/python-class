'''
word Frequency Analyzer
A company wants to analyze the text
write a python program:
1.Read contents from data.txt
2.Count the frequency of each word
3.Display most repeated word
4.Handle the exceptions

'''
try:
    with open("data.txt", "r") as file:
        words = file.read().lower().split()

    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    word = max(freq, key=freq.get)

    print("Most Repeated Word:", word)
    print("Frequency:", freq[word])

except FileNotFoundError:
    print("File not found")
