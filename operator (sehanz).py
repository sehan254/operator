#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num = 10
num2 = 3

jumlah = num1 + num2
kurang = num1 - num2
kali = num1 + num2
bagi = num1 /num2
bagi_bulat = num1 // num2
pangkat = num1 ** num2
modulus = num1 % num2


# In[ ]:


x = 5 #assigmen operator
x+10 # x = x + 10 => 15
print (x)
x-=4 # x = x -4 =>11
print (x)
x *=2 # x = x * 2 => 22
print (x)
x /=3 #x = x / 3 => 7...
print (x)
x //=2 #x = x// 2 => 3.0
print (x)
x **=3 #x = x ** 3 => 27
print (x)
x %=2 #x x % 2 => 1
print(x)

data =[1,2,3,4,5]
total = 0

for in range (0,5):
    total += data [i]

print("total :",total)


# In[5]:


bil1 = 8
bil2 = 7

is_equal = bil1 ==bil2
is_not_equal = bil1 != bil2
is_greater_than = bil1 > bil2
is_less_than = bil1 < bil2
is_greater_equal= bil1 >= bil2
is_less_equal = bil1  <= bil2

print(is_equal)
print(is_not_equal)
print(is_greater_than)
print(is_less_than)
print(is_greater_equal)
print(is_less_equal)


# In[7]:


var1 = 4
var2 =10

opr_and = var1 < var2 and var1 <=4 #true
opr_or = var1 >= var2 or var1 % 2==1 #False
opr_not = not opr_or
print(opr_and)
print(opr_or)
print(opr_not)


# In[11]:


fruits = ["Apple","Mangoes","Watermelon"]
my_favorite_fruits = fruits #Lokasi memori yang sama
your_fruits = ["Apple","Manggoes","Watermelon"]

print(fruits is my_favorite_fruits)
print(fruits is your_fruits)
print(fruits is not my_favorite_fruits)
print(fruits is not your_fruits)

a=5
b= 5 #phytton menggunakan metode asing dalam memberrikan nilai variale
print(a is b)
print(a is not b)


# In[12]:


student_names = ["Andi","Beni",'Chika']
print("Beni" in student_names)
print("Andi" not in student_names)
print("Chika" in student_names)
print("Davi" not in student_names)


# In[13]:


nilai_and = 255 & 15
nilai_or = 255 | 15
nilai_xor =255 ^ 15
# 11111111
# 00001111
# ---------xor
# 00001111 => 16 + 32 + 64 +128
print(nilai_and)
print(nilai_or)
print(nilai_xor)


# In[ ]:




