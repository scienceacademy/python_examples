import string
wordcount = {}
with open("alice.txt", "r") as f:
    data = f.read()
    words = data.split()
    for word in words:
        word = word.lower()
        for char in string.punctuation:
            word = word.replace(char, "")
        word = word.replace('"', "")
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
print(f"Number of words: {len(wordcount)}")
print(f"the: {wordcount['the']}")