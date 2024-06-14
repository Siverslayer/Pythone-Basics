tab = "-----------------------------------------"


#Break and Continue
#الكسور و الاكمال

#استخدام Break

while True :
    name = input("enter your name :")
    if name:
       print ("nice name MR. " , name) 
       break    
    else :
        print("enter your name :")

print(tab)
print(tab)




#استخدام Continue

num = input("enter the number 10-0 : ")
num = int(num)
some_number = 0

while some_number< 10 :
        some_number += 1
        if some_number == num : 
            continue
        print(some_number)


