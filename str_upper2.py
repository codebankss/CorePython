mes  = 'leader'

l = len(mes)
nmes = ''
for x in range(l):
  if mes[x] == 'd':
   nmes = nmes + mes[x].upper()
  else:
    nmes = nmes + mes[x].lower()

print(nmes)
