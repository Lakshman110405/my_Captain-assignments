import csv
def writeincsv(list1):
    with open('studentinfo.csv','a',newline='') as csvfile:
        writer= csv.writer(csvfile)
        if csvfile.tell()==0:
            writer.writerow(['Name','Class','Contact number','email id'])
        writer.writerow(list1)
if __name__=='__main__':
    s=1
    f=1
    while(f!=0):
        if f==1:
            n=input('Enter student {} Name class contact_number emailid with approriate spaces:'.format(s))
            list2=n.split(' ')
            print('the info is-name:{},class:{},num:{},email:{}'.format(list2[0],list2[1],list2[2],list2[3]))
            c=input('whter the entered values are right,yes or no:')
            if c=='yes':
                writeincsv(list2)
                s=s+1
                f=int(input('enter 1 to continue,0 to stop:'))
            elif c=='no':
                print('reenter the values')
                f=1
                
        
