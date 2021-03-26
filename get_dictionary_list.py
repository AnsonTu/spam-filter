def dictionaryList():
    f=open("dictionary.txt")

        
    dictionaryList = dict()

    for i in range (2500):
        x=f.readline()
        res=""
        for c in x:
            if c.isalpha():
                res="".join([res, c])
        dictionaryList[i]=res

    f.close() 
    return dictionaryList

