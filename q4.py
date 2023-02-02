# Q2 Answer template

N = int(input())
newVal=N
count = 0

if int(N)<10:
    count+=1
    newVal=N*10+N
    
while True:
    x1=newVal%10
    x2=((newVal//10)+(newVal%10))%10
    
    newVal=x1*10+x2
    count+=1
    
    if newVal==N:
        break
    
print(count)
