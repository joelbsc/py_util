# Given a integer n, returns the nth term of the fibonacci sequence
def fibonacci (x):
    try:
        if x > 1:
            fibo = fibonacci(x-1) + fibonacci(x-2)
        elif x == 1:
            fibo = 1
        else:
            fibo = 0

        return fibo 
    except:
        return 0

# Encode a given string with ceaser cipher method, in which each letter in the realtext is replaced 
# by a letter some fixed number of positions (steps) down the alphabet.
def caesarEncrypt(realText, step):
    try:
        if type(realText) != str or type(step) != int:
            raise TypeError

        ucase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lcase= ucase.lower()

        cipherText = ''

        for c in realText:
            if c.isalpha():
                if c in ucase:
                    cipherText += ucase[(ucase.index(c)+step)%26]
                else:
                    cipherText += lcase[(lcase.index(c)+step)%26]
            else:
                cipherText += c

        return cipherText

    except TypeError:
        print('Invalid parameters: realText must be a string and step must be an integer')

#It repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
def bubbleSort(pList):
    try:
        if type(pList) != list:
            raise TypeError

        for lastPos in range(len(pList)-1,0,-1):
            for i in range(lastPos):
                if pList[i]>pList[i+1]:
                    temp = pList[i]
                    pList[i] = pList[i+1]
                    pList[i+1] = temp

    except TypeError:
        print('Invalid parameters: pList must be a list')

#It takes the smallest element to the first position, after the second smallest to the second and so on.
def selectionSort(pList):
    try:
        if type(pList) != list:
            raise TypeError

        for firstPos in range(0, len(pList)-1):
            smallestPos=firstPos
            for i in range(firstPos+1,len(pList)):
                if pList[i]<pList[smallestPos]:
                    smallestPos = i
            temp = pList[firstPos]
            pList[firstPos] = pList[smallestPos]
            pList[smallestPos] = temp

    except TypeError:
        print('Invalid parameters: pList must be a list')

#It takes the nth element and put it in the correct position among the previous ones
def insertionSort( pList ):
    try:
        if type(pList) != list:
            raise TypeError

        for i in range( 1, len( pList ) ):
            num = pList[i]
            k = i
            while k > 0 and num < pList[k - 1]:
                pList[k] = pList[k - 1]
                k -= 1
            pList[k] = num

    except TypeError:
        print('Invalid parameters: pList must be a list')

#It starts by sorting pairs of elements far apart from each other, then progressively reducing the gap between elements to be compared.
#Here, the gap de sequence is simply determined by dividing the size of the sequence by 2.
def shellSort(pList):
    try:
        if type(pList) != list:
            raise TypeError

        gap = len(pList)//2
        while gap > 0:
            for startPosition in range(gap):
                for i in range(startPosition+gap,len(pList),gap):
            
                    currentValue = pList[i]
                    position = i
            
                    while position>=gap and pList[position-gap]>currentValue:
                        pList[position]=pList[position-gap]
                        position = position-gap
            
                    pList[position]=currentValue
                    
            gap = gap // 2

    except TypeError:
        print('Invalid parameters: pList must be a list')

#It divides the list into n sublists, each containing one element and repeatedly merge sublists, sorting it.
def mergeSort(pList):
    try:
        if type(pList) != list:
            raise TypeError

        if len(pList) > 1:
            mid = len(pList)//2
            left = pList[:mid]
            right = pList[mid:]  
            mergeSort(left)
            mergeSort(right)

            i = j = k = 0
        
            while i < len(left) and j < len(right): 
                if left[i] < right[j]: 
                    pList[k] = left[i] 
                    i+=1
                else: 
                    pList[k] = right[j] 
                    j+=1
                k+=1

            while i < len(left):
                pList[k]=left[i]
                i=i+1
                k=k+1
            while j < len(right):
                pList[k]=right[j]
                j=j+1
                k=k+1
                
    except TypeError:
        print('Invalid parameters: pList must be a list')


#It picks the last element as pivot and partitions the given array around the picked pivot,
#all smaller elements in the left and all greater ones in the right of the pivot.
def quickSort(pList):
    try:
        if type(pList) != list:
            raise TypeError

        if len(pList) > 1:
            pivot = i = len(pList)-1
            j = pivot-1

            while j >= 0:
                if pList[j] > pList[pivot]:
                    i=i-1
                    pList[i],pList[j] = pList[j],pList[i]

                j=j-1

            pList[pivot], pList[i] = pList[i], pList[pivot]

            left = pList[:i]
            right = pList[i+1:]  

            quickSort(left)
            quickSort(right)

            pList[:i] = left
            pList[i+1:] = right

    except TypeError:
        print('Invalid parameters: pList must be a list')       
