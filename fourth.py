#program to input a string and display only those which are at even indices

str = input(" Enter a string\n")
index = 0
while (index < len(str)):
  print( str[index],end='')
  index = index + 2