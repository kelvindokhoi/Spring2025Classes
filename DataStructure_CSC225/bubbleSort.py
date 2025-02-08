# bubbleSort

a=[*map(int,input().split())]
def isNotSorted(lst):
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            return True
    return False

def bubbleSort(lst):
    while isNotSorted(lst):
        for i in range(len(lst)):
            for j in range(len(lst)):
                if i<j and lst[i]>lst[j]:
                    lst[i],lst[j]=lst[j],lst[i]
    return lst

print(bubbleSort(a))