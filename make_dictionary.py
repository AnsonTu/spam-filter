import os
from collections import Counter

f = ['data/spam-test', 'data/spam-train'] #,'data/nonspam-test', 'data/nonspam-train']

for path in f:
    files = [os.path.join(path, f) for f in os.listdir(path)]
    words = []
    for file in files:
        with open(file) as mail: #open the email
            for i,line in enumerate(mail):
                w = line.split()
                words += w

    dictionary = Counter(words) #count frequency of each word
    wordsToRmv = dictionary.keys()
    for key in list(wordsToRmv): 
        if key.isalpha() == False:
            del dictionary[key]
        elif len(key) == 1: #get rid of single letter keys
            del dictionary[key]

    dictionary = dictionary.most_common(2500)

    textfile = open("dictionary.txt",'w')
    # print(dictionary)
    for w in dictionary:
        textfile.write(str(w[0]) + " " + str(w[1]) +"\n")
    textfile.close()