#binary
decimal=int(input("enter the decimal number: "))
def binary(n):
    if n>1:
        binary(n//2)
    print(n%2,end=" ")
#decimal number
binary(decimal)
print()
