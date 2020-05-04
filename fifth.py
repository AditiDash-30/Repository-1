#program to print all the prime numbers in a given interval & also to check if a given number is prime or not

lower = int(input(" Enter the lower range "))
upper = int(input(" Enter the upper range "))
          
for num in range(lower,upper+1):
  if(num>1):
    for i in range(2,num):
        if((num%i)==0):
           break
        else:
           print(num)
#now to check a number is prime or not
a = int(input("Enter  a number to if it's prime or not"))
j=1
if(a>1):
  for j in range(2,a):
    if((a%j)==0):
        print(a, " is not a prime number")
        break
    else:
        print(a," is prime")
else:
  print(a, " is not a prime number")
 
