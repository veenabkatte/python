#Bus chart 

chart=""
for row in range(1,8):
    for seat in range(1,5):
        amount=int(input("tell us total amount u have:"))
        if amount>=500:
            print("ur seat number:",row,seat)
            chart+="$"
        else:
            chart+="%"
            chart+="\n"
print(chart)
