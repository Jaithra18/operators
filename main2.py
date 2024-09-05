a=int(input("Enter an amount you want to withdraw"))
h=a//100
f=(a%100)//50
t=((a%100)%50)//10
tw=(((a%100)%50)%10)//2
print("the number of hundreds are",h,"\nthe number of fifties are",f,"\nthe number of tens are",t,"\nthe number of twos are",tw)