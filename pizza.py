#reading n and m
l=input().split()
n = int(l[0])
m = int(l[1])
l=input().split()
piz = []
for i in range(m):
    piz.append(int(l[i]))

#printing parsed values
print("N:",n,"M:",m)
print("")
print("L:",l)

def knpsck(a,itr,w):
    l=len(a)
    if itr==l:
        return 0
    if w <=0:
        return 0
    v1 = a[itr]+knpsck(a,itr+1,w-i)
    print(itr,":------------")
    v2 = knpsck(a,itr+1,w)
    ret = max(v1,v2)
    print("itr: ",itr, "w: ",w,"ret: ",ret)
    return ret
out = knpsck(piz,0,17)
print(out)
