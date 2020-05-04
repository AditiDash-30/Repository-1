#program to count the total digits in a given number

n = int(input(" Enter a number to calculate the no of digits in it"))
c=0
while(n>0):
  c = (c+1)
  n = (n//10)
print(" The number of digits in the given number are",c)
