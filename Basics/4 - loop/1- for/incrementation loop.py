tab = "--------------------------------------------------------------------------"



#متغير قيمته 0
num0 = 0

print (num0)

#قم ب اضافه رقم 1 الى المتغير 
num0 += 1

#طباعه المتغير بعد الاظافه
print (num0)



print (tab)



#حساب عدد الاحرف في الاسم

#الاسم
name = "Mohammed"

#متغير يمثل رقم 0
x = 0

#بدأ عمليه التكرار
for letter in name:

#اضف رقم 1 على المتغير X
    x += 1

#طباعه الناتج النهائي
print (name , "has" , str (x) , "letters")




print (tab)



#انشاء لست تحتوي على اسماء و طباعة عدد تلك الاسماء


names = ["Ali" , "Ahmed" , "Mohammmed" , "LAMA" , "HUSSEN" , "HUSEEN"]

xx = 0

for name1 in names:
    xx += 1

print(xx)




print (tab)


#انشاء برنامج بسيط يطلب من الشخص ادخال اسمه ثم طباعه عدد الاحرف

#طلب ادخال الاسم
your_name = input ("your name :") 

#متغير يرمز للرقم 0
xxx=0

#انشاء عمليه تكرار
for aaa in your_name :
 #اضف رقم 1 للمتغير xxx
    xxx +=1

#اطبع قميه المتغير xxx في الناتج النهائي لها
print ("the number of letters in your name = " , xxx)