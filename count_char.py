def str1(x):
  l = len(x)
  for i in range(l):
    j = 0
    count = 0
    for x[j] in x:
      if x[j] in x:
        count += 1
        print(x[j], 'is', count, 'times')
    j += 1

