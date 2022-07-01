import time


# UnRecursive Iteration
def factorial(n):
  response = 1

  while n > 1:
    response *= n
    n -= 1

  return response


# Recursive Iteration
def r_factorial(n):
  if n == 1:
    return 1

  return n * r_factorial(n - 1)


def main():
  n = 1000

  start = time.time()
  factorial(n)
  end = time.time()
  print(end - start)

  start = time.time()
  r_factorial(n)
  end = time.time()
  print(end - start)


if __name__ == "__main__":
  main()

