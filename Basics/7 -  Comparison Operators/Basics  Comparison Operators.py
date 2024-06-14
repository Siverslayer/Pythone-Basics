#--------------------------------------------*
# == يطابق                                   *
# != لا يطابق                                 *
# > اكبر من                                  *
# < اصغر من                                  *
# >= اكبر من او يساوي                       *
# <= اصغر من او يساوي                       *
#--------------------------------------------*
tab = "--------------------------------------------"




test = 1==1
print (test)

print (tab)

test = 1!=1
print (test)

print (tab)


test = 1>=1
print (test)


print (tab)


test = 1<=1
print (test)


print (tab)



name = "ali"
name1 = input ("what's your name? ")

if name1.lower() == name:
   print ("ok MR." , name , ", you can take the key ")
else:
   print("ok MR.", name1 ,", you can not take the key ")

print (tab)

print (tab)

print (tab)



name2 = "ahmed"
name3 = input("What's your name? ").lower()


#هنا قمنا بعكس عمليه المقارنه حيث لم نبدأ ب  name2 بل ب name3
if  name3.lower != name2.lower() :
   print("OK MR.", name2, ", you can not take the key")
else:
   print("OK MR.", name3, ", you can take the key")