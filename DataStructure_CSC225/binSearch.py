def binSearch(theList,lo,hi,x):
    if lo>=hi:
        return False
    mid=(hi+lo)//2
    if theList[mid]==x:
        return True
    if theList[mid]<x:
        return binSearch(theList,mid+1,hi,x)
    else:
        return binSearch(theList,lo,mid-1,x)
        
theList=[-1,0,9,18,22,50,93,99,102]
print(binSearch(theList,0,len(theList),int(input())))