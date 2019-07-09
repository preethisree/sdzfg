s1 = input()
s1 = list(s)
stl = ''.join(s)
stl = stl.strip()
rev = s1[::-1]
reversed = ''.join(rev)
reversed = reversed.strip()
if (stl==reversed):
  print('YES')
else:
  print('NO')
