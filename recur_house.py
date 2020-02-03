#recursive


warehouse=[0]

def details(index=0):
    if index<len(warehouse):
        print(warehouse[index])
        index+=1;details(index)
    else:
        return

def update(index=0,end=len(warehouse)):
    if index<end:
        decide=input("tell us what you wish to do: ")
        if decide=="take":
            amt=int(input("tell us money wish to take: "))
            if amt>=warehouse[index]:
                warehouse.append(0)
            else:
                warehouse.append(warehouse[index]-amt)
        elif decide=="give":
            amt=int(input("tell us money wish do give: "))
            warehouse.append(warehouse[index]+amt)
        else:
            print("check the amount alter")
        index+=1;update(index,end)
    else:
        return
    
def findNPut(index=0,end=len(warehouse),count=0,fee=0):
    if index<end:
        if warehouse[index]=="debit":
            count+=1;
            if count>=2:
                fee-=20
        index+=1;findNPut(index,end,count,fee)
    else:
        print("charges for this month is: ",fee);return


update(0,5)
details()
findNPut(0,len(warehouse));
