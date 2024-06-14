#input ما يدخله المستخدم
#و كيف تاحقق منه 




#تجربه صنع برنامج بكلمة مرور 
#كلمه سر

my_ps = 123


ps = input("enter ps :")


if ps == str (my_ps) :
    print ("good")
else :
    print ("?????")





#تجربه عمل اله جمع بسيطه

num1 = input ("num 1 :")
num2 = input ("num 2 :")

print (int (num1) +int (num2))





#دمج اله الجمع مع برنامج كلمه  السر


my_ps2 = 111


ps2 = input("enter ps :")


if ps2 == str (my_ps2) :
    num3 = input ("num 1 :")
    num4 = input ("num 2 :")
    print (int (num1) +int (num2))
else :
    print ("?????")
