str1 = 'AAAlBBBaCCCoDDDzEEEhFFFaGGGnGGGgfdasfasldfkedfkjlaijklfasdkjfiasdfje'
countA = 0
countB = 0
countC = 0
length = len(str1)

for i in range(length):
    if str1[i] == '\n':
        continue

    if str1[i].isupper():
        if countB:
            countC += 1
        else:
            countC = 0
            countA += 1


    if str1[i].islower():
        if countA != 3:
            countA = 0
            countB = 0
            countC = 0
        else:
            if countB:
                countC = 0
                countB = 0
                countA = 0
            else:
                countB = 1
                countC = 0
                target = i


    if countA == 3 and countC == 3:
        if i+1 != length and str1[i+1].isupper():
            countC = 0
            countB = 0
        else:
            print(str1[target], end='')
            countA = 3
            countB = 0
            countC = 0

