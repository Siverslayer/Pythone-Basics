
# العوامل المنطقية في بايثون: `not` و `and` و `or`

مرحبًا بكم في هذا الدليل المبسط حول العوامل المنطقية في بايثون! 🎉

العوامل المنطقية هي أدوات قوية تُستخدم في البرمجة للتحكم في تدفق البرنامج واتخاذ القرارات بناءً على شروط معينة. في هذا الدليل، سنستعرض العوامل المنطقية الأساسية في بايثون: `not` و `and` و `or`.

## المحتويات
- [العامل المنطقي `not`](#العامل-المنطقي-not)
- [العامل المنطقي `and`](#العامل-المنطقي-and)
- [العامل المنطقي `or`](#العامل-المنطقي-or)


## العامل المنطقي `not`

العامل `not` هو عامل منطقي أُحادي (Unary operator) يُستخدم لعكس القيمة المنطقية.

- إذا كانت القيمة هي `True`، فإن `not` يجعلها `False`.
- إذا كانت القيمة هي `False`، فإن `not` يجعلها `True`.

### مثال
```python
a = True
print(not a)  # Output: False

b = False
print(not b)  # Output: True
```

## العامل المنطقي `and`

العامل `and` هو عامل منطقي ثنائي (Binary operator) يُستخدم للتحقق من صحة كلا التعبيرين المنطقيين.

- يُرجع `True` فقط إذا كانت كلا التعبيرين صحيحة (`True`).
- إذا كانت أي من التعبيرين `False`, يُرجع `False`.

### مثال
```python
a = True
b = False
print(a and b)  # Output: False

c = True
d = True
print(c and d)  # Output: True
```

## العامل المنطقي `or`

العامل `or` هو عامل منطقي ثنائي (Binary operator) يُستخدم للتحقق من صحة أي من التعبيرين المنطقيين.

- يُرجع `True` إذا كان أي من التعبيرين صحيح (`True`).
- يُرجع `False` فقط إذا كانت كلا التعبيرين خاطئة (`False`).

### مثال
```python
a = True
b = False
print(a or b)  # Output: True

c = False
d = False
print(c or d)  # Output: False
```

## أمثلة عملية

### مثال 1: التحقق من صلاحية المستخدم

في هذا المثال، نستخدم العاملين `and` و `not` للتحقق من اسم المستخدم وكلمة المرور. إذا كان كلاهما صحيحًا، يتم منح الوصول؛ وإلا، يتم رفض الوصول.

```python
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Access granted!")
else:
    print("Access denied!")
```

### مثال 2: التحقق من سن الدخول

في هذا المثال، نستخدم العامل `or` للتحقق مما إذا كان الشخص يمكنه الدخول بناءً على العمر أو وجود إذن خاص.

```python
age = 20
has_permission = True

if age >= 18 or has_permission:
    print("You can enter!")
else:
    print("Entry denied!")
```

### مثال 3: عكس حالة المصباح

في هذا المثال، نستخدم العامل `not` لعكس حالة المصباح من مطفأ إلى مضاء أو العكس.

```python
is_light_on = False
is_light_on = not is_light_on  # يقلب حالة المصباح
print(is_light_on)  # Output: True
```

### مثال 4: التحقق من القيم المتعددة

في هذا المثال، نستخدم العامل `and` للتحقق مما إذا كانت كل القيم في القائمة صحيحة.

```python
values = [True, True, True]

if all(values):
    print("All values are True")
else:
    print("Not all values are True")
```

### مثال 5: التحقق من وجود قيمة معينة

في هذا المثال، نستخدم العامل `or` للتحقق مما إذا كانت أي قيمة في القائمة صحيحة.

```python
values = [False, False, True]

if any(values):
    print("At least one value is True")
else:
    print("All values are False")
```

## المصادر الإضافية

لمزيد من المعلومات حول العوامل المنطقية في بايثون، يمكنك زيارة المصادر التالية:

- [التوثيق الرسمي لبايثون](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not): يحتوي على تفاصيل شاملة حول العمليات المنطقية في بايثون.
- [دروس بايثون على موقع W3Schools](https://www.w3schools.com/python/python_operators.asp): يوفر شرحًا مبسطًا وسهل الفهم حول العوامل المنطقية وأمثلة تطبيقية.
- 
نتمنى أن يكون هذا الدليل قد ساعدك في فهم العوامل المنطقية في بايثون 
