
def check_version(v1,v2):

    if v1==None or v2==None or len(v1)==0 or len(v2)==0:
        return 0
    
    l1 = [int(i) for i in v1.split(".")]
    l2 = [int(i) for i in v2.split(".")]

    while(len(l1)<len(l2)):
        l1.append(0)

    while(len(l1)>len(l2)):
        l2.append(0)

    i=0
    while i<len(l1) and i<len(l2):

        if l1[i]>l2[i]:
            return 1
        elif l1[i]<l2[i]:
            return -1
        
        i+=1


    return 0



v1 = input()
v2 = input()

print(check_version(v1,v2))
    