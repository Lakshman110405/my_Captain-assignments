def most_frequent(n):
    a={}
    for i in n:
        if(i in a):
            a[i]+=1
        else:
            a[i]=1
    c=sorted(a.items(),key=lambda x:x[1],reverse=True)
    for letter,frequency in c:
        print(letter,':',frequency,end=',')
    print('\b.')
n=input('enter a string:')
most_frequent(n)