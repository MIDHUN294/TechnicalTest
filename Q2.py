a=str(input("Enter the string:"))
b=str(input("Enter the substring:"))
count=0
for i in range(len(a)):
 if a[i:].startswith(b):
  count+=1
print (count)