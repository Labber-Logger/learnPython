f = open("words.txt", "r")
text = f.read()

def makeSet(text):
    list = text.split(' ')
    words = dict()
    for w in list:
        words[w] = True
    print words

# makeSet(text)

def countOccurrences(text):
    list = text.split(' ')
    words = dict()
    for w in list:
        if w in words:
            words[w] = words[w] + 1
        else:
            words[w] = 1
        print words
    print words


countOccurrences(text)
