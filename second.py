#program to accept 'n' no. fom user & calculate sum of all numbers between i& n including

n = input("Enter number to calculate sum")
n = int(n)
sum = 0
for num in range (0, n+1, 1):
      sum = sum+num
print("Sum of the first",n," numbers is-",sum)
