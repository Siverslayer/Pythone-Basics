

## شرح الرسائل النصية (Strings) في Python

## في Python، يمكنك استخدام كل من علامة التنصيص المفردة (') والمزدوجة (") لكتابة الرسائل النصية. هذا يسهل تضمين علامات تنصيص مختلفة داخل الرسالة نفسها:

```python
print("It's alright")  # استخدام علامات تنصيص مزدوجة
print('He is called "Johnny"')  # استخدام علامات تنصيص مفردة
print("He is called 'Johnny'")  # استخدام علامات تنصيص مزدوجة
```

### إضافات:

* **الجمع بين الرسائل النصية (Concatenation):**

```python
greeting = "Hello"
name = "Sarah"
print(greeting + ", " + name + "!")  # Output: Hello, Sarah!
```

* **تكرار الرسائل النصية (Repetition):**

```python
message = "Echo... "
print(message * 3)  # Output: Echo... Echo... Echo... 
```

## طباعة النصوص (Printing)

```python
a = "hello world"
print(a)
```

### إضافات:

* **تنسيق الطباعة (Formatted Printing):**

```python
name = "Ahmed"
age = 25
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Ahmed and I am 25 years old.
```

* **طباعة متغيرات متعددة:**

```python
city = "Riyadh"
country = "Saudi Arabia"
print("I live in", city, ",", country)  # Output: I live in Riyadh , Saudi Arabia
```

## الوصول إلى حروف النص (Indexing)

```python
a = "hello world"
print(a[1])  # Output: e 
```

### إضافات:

* **الوصول إلى الحروف من النهاية:**

```python
print(a[-1])  # Output: d (الحرف الأخير)
print(a[-2])  # Output: l (الحرف قبل الأخير)
```

* **تقطيع النصوص (Slicing):**

```python
print(a[0:5])  # Output: hello (الحروف من 0 إلى 4)
print(a[7:])   # Output: orld (الحروف من 7 إلى النهاية)
```

## دالة `len`

```python
a = "Hello, World!"
print(len(a))  # Output: 13
```

### إضافات:

* **التحقق من كون النص فارغًا:**

```python
text = ""
if len(text) == 0:
    print("The text is empty.")
```

* **مقارنة أطوال النصوص:**

```python
word1 = "apple"
word2 = "banana"
if len(word1) > len(word2):
    print("The word 'apple' is longer.")
```
