#simple if and else
#ssquarefeet,pincode

square_feet=float(input("tell us the squqre_feet : "))
pincode=int(input("tell us  pincode of city : "))
if square_feet<=4 or  square_feet<=1 and pincode==574240:
   print("registration charges is:2400")
elif square_feet<=8 or  square_feet<=4 and pincode==584219:
    print("registration charges is:3600")
elif square_feet>=12 or  square_feet<=8 and pincode==598765:
    print("registration charges is:4800")
 
else:
       print(" sorry,enter valid ")
