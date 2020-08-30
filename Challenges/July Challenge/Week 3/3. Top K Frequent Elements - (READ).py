nums = [int(i) for i in input().split()]
k = int(input())

d = {}

for i in nums:
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1

arr = []

for n in d.keys():
    arr.append([n,d[n]])

# Sortig acc to freq
arr.sort(key=lambda x: x[1],reverse=True)

for n,f in arr[0:k]:
    print(n,end=" ")

print()
