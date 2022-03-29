import week0.swap as swap


def fibterm(a, b, n):
  if n == 1:
    return a
  elif n == 2:
    return b
  elif n > 2:
    return fibterm(a, b, n - 1) + fibterm(a, b, n - 2)
def term():
  a = int(input("What is the starting number going to be?\n"))
  b = int(input("What is the second number going to be?\n"))
  n = int(input("Which nth term do you want to print?\n"))
  a, b = swap.sort(a, b) 
  print(fibterm(a, b, n))
def seq():
  a = int(input("What is the first number?\n"))
  b = int(input("What is the second number going to be?\n"))
  n = int(input("What term do you want to print?\n"))
  a, b = swap.sort(a, b)
  print(", ".join([str(fibterm(a, b, i + 1)) for i in range(0, n)]))