import math

print(end="Enter the Value of n: ")
n = int(input())
for i in range(n):
  for col in range(n-1, i, -1):
    print(end=" ")
  for col in range(i+1):
    val = int(math.factorial(i)/(math.factorial(col)*math.factorial(i-col)))
    print(val, end=" ")
  print()