myfile = open(r"GET FULL PATH OF FILE HERE")
wordlist = []
countlist = []
lines = {}
linenumber = 0
for aline in myfile:
    linenumber += 1
    linelist = aline.split()
    for aword in linelist:
        aword = ''.join(filter(str.isalnum, aword)).lower()
        if aword not in wordlist:
            wordlist.append(aword)
            countlist.append(1)
            lines[aword] = [linenumber]
        else:
            countlist[wordlist.index(aword)] += 1
            if linenumber not in lines[aword]:
                lines[aword].append(linenumber)

for i in range(len(wordlist)):
    print("'"+ wordlist[i] + "'","appears",countlist[i], "times at line", " ".join(str(j) for j in lines[wordlist[i]]))
myfile.close()
