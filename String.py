## Code for string basics
str = "Priya Tambe"
print(str)
print(len(str))
print (str.lower())
print(str.upper())
print(str+"okok")
print(str[0:2])

num=7
print(num)
if (num>5):
    print("yes greater")
else:
    print("no")


for i in range (num):
     print(i)


print("STop")
for i in range (num):
    if (i==2):
        continue
    if (i==5):
        break
    print(i)