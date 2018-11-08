i = int(input("Enter 1 number"))
j = int(input("Enter number 2"))

try:
  k = i/j
  print("Total", k)
except ZeroDivisionError as ze:
  print(ze)
finally:
  print("Must")

print("Running")
