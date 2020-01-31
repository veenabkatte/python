#to remove the number of string

string=input("enter the string")
start=int(input("enter the string index"))
end=int(input("enter the end index"))
if len(string)>end:
    string=string[:start]+string[end+1::]
print(string)
