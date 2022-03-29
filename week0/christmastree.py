def tree(n, p):
  z = n - 1
  x = 1
  for i in range(0, n):
    print(' ' * z, f'{p} ' * x, ' ' * (z - 1))
    x += 1
    z -= 1
  if n // 3 % 2 == 1:
    y = n // 3 + 1
  else:
    y = n // 3
  for i in range (0, y):
    print(' ' * (n - (y //2 + 1)), f'{p}' * (y + 1), ' ' * (n - (y //2 + 1)))


def options():
  try:
    n = int(input("How tall do you want your Christmas tree to be?\n"))
    p = input("What character do you want your tree to be made out of?\n")
    tree(n, p)
  except:
    print("How tall means u gotta put in a number :/")