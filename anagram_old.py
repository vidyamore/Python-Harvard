def wordIterator(dictionaryFilename):
    with open(dictionaryFilename,'r') as f:
        for line in f:
            word = line.strip()
            yield word

def largestAnagram(words):
    import collections
    d = collections.defaultdict(list)
    for word in words:
        sortedWord = str(sorted(word))
        d[ hash(sortedWord) ].append(word)
    maxKey = max( d.keys(), key = lambda k : len(d[k]) )
    count =0
    while (maxKey != 0):
        maxKey = max( d.keys(), key = lambda k : len(d[k]) )
        print(d[maxKey])
        del d[maxKey]
        count = count +1
        if count > 10:
            break
    return d[maxKey]

ter = wordIterator( 'words.txt' )
largestAnagram(ter)