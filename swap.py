n =[93,51,45,12]
x=4
i=0
for i in range(0,x):
    first_digit = n[i]//10
    second_digit = n[i]%10
    swapped_number = (second_digit*10)+first_digit
    print (swapped_number)
    i+=1
