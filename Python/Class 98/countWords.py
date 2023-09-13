def countWordsFromFile():
    fileName=input("Enter the file name:")
    words=0
    file=open(fileName)
    for i in file:
        num=i.split()
        words=words+len(num)
    print(words)

countWordsFromFile()