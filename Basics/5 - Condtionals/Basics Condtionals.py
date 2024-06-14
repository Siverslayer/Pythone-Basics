#الشروط

#انشاء برنامج  يسمح لاشخاص الذي اعمارهم 16 فما فوق ب الانظمام الى  مجموعه
#و التأكد من اجابتهم اذا كانت نعم ام لا

url = "x"
age = input ("enter your age : ")
age1 = int(age)


if age1 > 15:
    print("good")
else:
    print("you cannot join the group")
    exit()

yes_no = input ("are you sure to join the group?")

if yes_no.lower() == "yes" :
   print ("url : " , url)
elif yes_no.lower() == "no" :
   print ("ok")
else :
   print ("just yes/no")
