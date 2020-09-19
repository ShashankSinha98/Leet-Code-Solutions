# TODO-Complete It

res = set()
def solve(arr,target,ans):
    global res
    if target == 0:
        ans.sort()
        res.add(str(ans))
        return 
    
    if target<0:
        return
    
    for i in arr:
        ans += [i]
        solve(arr,target-i,ans)
        ans.remove(i)
    
arr = [2,3,5]
target = 8

solve(arr,target,[])
print(res)