arr = [int(i) for i in input().split()]


def solve(arr):
    n = len(arr)
    dp = []

    for i in range(2**n):
        s = ""
        for j in range(n):
            if(i & (1<<j))!=0:
                s+=str(arr[j])+" "

        if s not in dp:
            dp.append(s)
    
    res = []
    for i in dp:
        res.append([int(j) for j in i.split()])

    return res



arr.sort()
res = solve(arr)
res.sort()
print(res)