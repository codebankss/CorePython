a = int(input("Enter a number between 1 to 9"))
b = a*2
c = b + 5
d = c*50
e = str(input("Have u had your birthday?"))

if(e == "yes" or e=="Yes" or e=="Yes"):
    f = d + 1767
else:
    f = d + 1766

g = int(input("Enter the year of your birth"))
 
h = f - g

print("Age is", ((h%100)+1))
i = round(h/100)
print("input number is", i)
