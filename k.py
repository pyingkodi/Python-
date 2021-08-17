a=[50,55,45,66,77,568,85,654,55555]
for i in range(0,len(a)):
    n=a[i]
    while(n>0):
        rem=n%10
        n=n//10
        
    if(rem==5):
        print(a[i])    
    
