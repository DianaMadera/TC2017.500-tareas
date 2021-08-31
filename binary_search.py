import random

values = []
for i in range(1,10):
    values.append(random.randint(1, 10))
values.sort()
print ( values)
def binary(vals,k):
    l=0
    r=len(vals)-1
    while l<=r:
        m=(l+r)//2
        if k== vals[m]:
            return m
        elif k<vals[m]:
            r=m-1
        else:
            l=l+1

print(binary(values,3)) 

