


def a_quickSort(lst): #Making-a-list Quick Sort
    if len(lst)<2:
        return lst
    pivot=lst[0]
    a=[]
    b=[]
    for i in range(1,len(lst)):
        if lst[i]<pivot:
            a.append(lst[i])
        else:
            b.append(lst[i])
    return a_quickSort(a)+[pivot]+a_quickSort(b)

def b_quickSort(lst,low=0,high=None):  #In-place Quick Sort
    if high==None:
        high = len(lst)-1
    if low<high:
        pivot_index = low
        pivot=lst[pivot_index]
        i=low+1
        j=high
        while True:
            while i<=j and lst[i]<=pivot: i+=1
            while i<=j and lst[j]>=pivot: j-=1
            if i<=j: lst[i],lst[j]=lst[j],lst[i]
            else: break
        # lst[low],lst[j]=lst[j],lst[low]
        pivot_index=j
        b_quickSort(lst,low,pivot_index-1)
        b_quickSort(lst,pivot_index+1,high)

def partition(lst,lo,hi):
    pivot=lst[hi]
    i=lo
    for j in range(lo,hi):
        if lst[j]<=pivot:
            lst[i],lst[j]=lst[j],lst[i]
            i+=1
    # lst[i],lst[hi]=lst[hi],lst[i]
    return i
def c_quickSort(lst,lo,hi): #Wikipedia version
    if lo>=hi or lo<0:
        return 0
    p=partition(lst,lo,hi)
    c_quickSort(lst,lo,p-1)
    c_quickSort(lst,p+1,hi)




while True:
    try:
        lst1 = [int(x) for x in map(int, input("🧙‍ *Wizard waves wand* Gimme your hardest spell (numbers separated by spaces): ").split())]
    except ValueError:
        print("\n🧙 *Wizard frowns* 'Tis not a valid spell! I see non-magical numbers in your incantation! 🪄")
        print("✨ *Poof!* The spell fizzles out. Try again with proper integers, mortal!\n")
        exit(0)
    # print("\n✨ *Poof!* Here is your spell sorted with magic (but not space-efficient):", a_quickSort(lst))
    c_quickSort(lst1,0,len(lst1)-1)
    print(lst1)
    # b_quickSort(lst)
    # print("✨ *Poof again!* Here is your spell sorted with space-efficient wizardry:", lst)
    # print("🧙 *Wizard grins* Ready for another spell? Or are you out of magic? 🪄\n")



