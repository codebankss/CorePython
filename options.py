li = []
ans = 'y'
while ans == 'y':
  print("1. Add'', 2. Show, 3. Search, 4. Update, 5. Delete,6. Exit")

  ch = int(input())
  if ch == 1:
    x = int(input("Enter record"))
    li.append(x)

  elif ch == 2:
    print(li)

  elif ch == 3:
    x = int(input("Enter record for search"))
    if x in li:
      print("Record found")
    else:
      print("Record not found")

    elif ch == 4:
      i = int(input("Enter record to change"))
      j = int(input("Enter changed record"))
      if i in li:
        x = li.index(i)
        li.remove

      
      

