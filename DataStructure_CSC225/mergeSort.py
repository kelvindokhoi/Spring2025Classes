def merge(a, b):
    len1,len2=len(a),len(b);after=[0]*(len1+len2);c1=c2=0
    for i in range(len1 + len2):
        if c1 == len1:after[i:]=b[c2:];break
        if c2 == len2:after[i:]=a[c1:];break
        if a[c1]<b[c2]:after[i]=a[c1];c1+=1
        else:after[i]=b[c2];c2+=1
    return after

def mergeSort(a):
    if len(a) < 2:return a
    else:mid=len(a)//2;return merge(mergeSort(a[:mid]),mergeSort(a[mid:]))
while 1:
    print(mergeSort([*map(int,input("Gimme your hardest test case: ").split())])) #normal

while 1:
    print([mergeSort([int(ord(x)) if type(x)==str else x for x in input("Gimme your hardest test case: ").split()  ])])