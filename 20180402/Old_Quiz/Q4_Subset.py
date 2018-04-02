a,b=input().split()
array=[]
for c in a: array.append(c)
include=[0 for i in range(len(array))]
l = len(array)
ascii=[]
total=0

def power_set(k):
    global arr,include,l,ascii,total
    if k == l:
        summ=0
        for i in range(l):
            if include[i]: summ+=ord(array[i])
        ascii.append(summ); total+=1; return
    include[k]=False; power_set(k+1); include[k]=True; power_set(k+1)
    
            

power_set(0)
print(total, end=" ")

total2=0
for items in ascii:
    if items%int(b)==0:
        total2+=1
print(total2)
