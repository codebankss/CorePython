n = input()

l = len(n)
count = 0

for x in range(l):
  if (n[x] == 'a'):
    count +=1

print('a is repeated', count, 'times')
