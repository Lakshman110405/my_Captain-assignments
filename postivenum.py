n=int(input('Enter a integer:'))
list1=[]
while(n!=00):
    list1.append(n)
    n=int(input('Enter a integer to add to a list,enter 00 to stop:'))
print(list1)
for i in  list1:
    if(i>0):
        print(i,end=',')
print('\b.')