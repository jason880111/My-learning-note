def quicksort(mylist):
    smaller = []
    bigger = []

    if len(mylist) <= 1:
        return mylist

    else:
        pivot = mylist[0] #第一個數為pivot
        for i in mylist:
            if i < pivot: #比基準值小的數
                smaller.append(i)
            elif i > pivot: #比基準值大的數
                bigger.append(i)

    smaller = quicksort(smaller)
    bigger = quicksort(bigger)
    return smaller + [pivot] + bigger
    
    list = [5, -8, -15, -23, 0, 3, 14, -5, 10, 28]
    quicksort(list)
    [-23, -15, -8, -5, 0, 3, 5, 10, 14, 28]
