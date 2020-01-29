#reverse numer
num=int(input("enter a number"))
print(num)
rev=0
while(num>0):
        remainder=num %10
        rev = (rev*10)+remainder
        num = num//10
        print("the reversed number is",rev)
      

      
