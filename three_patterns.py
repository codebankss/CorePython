def pattern1(Symbol, n):
  
  for i in range (0, n):              #defining number of rows
    for j in range(0, i+1):          # to print the symbol till i+1 in a row
      print(Symbol, end = "")     #printing the symbol number of times defined and ending with space
    print('\n')                              #continuing in next line after single execution of the loop

  for i in range (1, n):              #no. of rows starting from 1 since non repeating peak
      for j in range(0, n-i):          # decreasing after peak and printing after n-i
          print(Symbol, end='')
      print("\n")

print("Non repeating peak")
pattern1('#', 11)

print("-"*50)


def pattern2(Symbol, n):
  
  for i in range (0, n):
    for j in range(0, i+1):
      print(Symbol, end = "")
    print('\n')

  for i in range (0, n):
      for j in range(0, n-i):
          print(Symbol, end='')
      print("\n")



print("Repeating peak")
pattern2("*", 6)

print("-"*50)


def pattern3(Symbol, n):
  for i in range(0, n):           #rows from 0 to n
    for j in range(0, n-i-1):    #for printing dots till n-i-1
      print( end = ".")     
    for j in range(0, i+1):     #no. of times to print the symbol
      print(Symbol, end = "")#to print the symbol      
    print("\n")

  for i in range(0, n-1 ):
    for j in range(0, i+1):
      print(end = ".")
    for j in range(0, n-i-1):
      print(Symbol, end = "")
    print("\n")
    
pattern3('7', 10)
  
