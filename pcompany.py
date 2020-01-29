#simple if and else
#skill set,project

skill_set=input("tell us ur  skill : ")
project=int(input("tell us ur  no of project done : "))
if skill_set=="c" or  skill_set=="java" and project>=2:
   print("u can get  job in EVERYINDIA")
elif skill_set=="C++" or  skill_set=="java" and project>=3:
    print("u can get job in TCS")
elif skill_set=="java"or  skill_set=="python" and project>=4:
    print("u can getjob in INFOSIS")
elif skill_set=="python" or skill_set=="c" and project>=6:
    print("u can getjob in ZOHO")  
else:
       print(" sorry u can't ")
