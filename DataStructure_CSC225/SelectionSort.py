def selectionSort(List):
    pointer=0
    hi=len(List)
    for i in range(hi):
        currlo=List[pointer]
        lopoint=pointer
        for j in range(lopoint+1,hi):
            if List[j]<currlo:
                currlo=List[j]
                lopoint=j
        List[pointer],List[lopoint]=currlo,List[pointer]
        pointer+=1
while 1:
    List=[*map(int,input("Enter your funny numbers: ").split())]
    selectionSort(List)
    print(List)
