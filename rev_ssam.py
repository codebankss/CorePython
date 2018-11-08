def rev(x):
  reverse = 0
  while(x>0):
    r = x%10
    reverse = reverse*10 +r
    x = x//10
  return reverse
  
