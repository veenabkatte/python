#bank charges
count=0
amount=int(input("enter the amount in ur accoynt: "))
for yet in range(1,11):
    decide=input("tell us what u wish to do: ")
    if decide=="deposit":
        money=int(input("tell us money u want to deposit:"))
        amount+=money
        print("amount in ur account after transaction: ",amount)
    elif decide=="withdraw":
        money=int(input("tell us money you want to withdraw: "))
        if count<5:
            amount-=money
            print("amount in ur account after transaction:",amount)
        else:
                amount-=money+20
                print("amount in ur account after transaction: ",amount)
        count+=1
           
