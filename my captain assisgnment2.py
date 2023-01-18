n=int(input('enter the maximum range num:'))
f=0
s=1
sum=0
print(f,s,end=',')
while(s<n):
    sum=f+s
    print(sum,end=',')
    f=s
    s=sum
