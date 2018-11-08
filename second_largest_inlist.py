n = int(input())
li = []
for i in range(n):
    num = int(input())
    li.append(num)

print(li)

li2 = []
for j in li:
    if j not in li2:
        li2.append(j)

print(li2)

li2.sort()
print(li2)
print(li2[n-2])

