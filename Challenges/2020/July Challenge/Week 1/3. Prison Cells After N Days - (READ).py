def prisonAfterNDays(cells, N):

    storage = set()
    isRepeating = False
    nextDayCell  = []
    tempCells = cells

    for i in range(0,N):

        nextDayCell = nextDay(tempCells)
        if not str(nextDayCell) in storage:
            storage.add(str(nextDayCell))
        else:
            isRepeating = True
            break
        
        tempCells = nextDayCell

        
    
    
    
    if(isRepeating):
        pos = N%len(storage)
        for i in range(1,pos+1):
            tempCells = nextDay(tempCells)

    return tempCells


    

def nextDay(cells):
    n = len(cells)
    res = [0 for i in range(n)]
    for i in range(1,n-1):

        if cells[i-1]==cells[i+1]:
            res[i]=1
       
    
    return res


arr = [int(i) for i in input().split()]
N = int(input())

print(prisonAfterNDays(arr,N))

