import array as arr
a=arr.array('i',[20,25,30,35,40,45,89,69,1236,488,634])
for i in range(0,len(a)):
    while(a[i]!=0):
        rem=a[i]%10
        a[i]=a[i]//10
    print(rem)
