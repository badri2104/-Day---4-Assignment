# Q1. Python program to print Highest Common Factor (HCF) of two numbers
x = 50
y = 100
if x > y:
  x, y = y, x
for i in range(1,x+1):
  if x%i == 0 and y%i == 0:
    hcf = i

print("HCF of", x, "and", y, "is:", hcf)
