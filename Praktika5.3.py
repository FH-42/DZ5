
def words():
    text = open('Praktika5.3(1)', 'r')
    dict1 = {}
    for line in text:
        words = line.split()
        # a = list(text)
        #textl = text.read().lower()
        for word in words:
            # print(word)
            if dict1.get(word):
                dict1[word] += 1
            else:
                dict1[word] = 1

    for item in sorted(dict1):
        print(item, dict1[item])

    #textl = []
            #map(words, textl)
    # dict1.update(list(map(lambda x: words(''.join(filter(str.isalpha, x.lower())), a.split()))))
    # print(dict1)
words()