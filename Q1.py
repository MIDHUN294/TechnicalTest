var1=int(input("enter the 1st number:"))
var2=int(input("enter the 2nd number:"))
print("Before swapping var1=\t{}\tvar2 =\t{}\n".format(var1,var2))
var1=var1+var2
var2=var1-var2
var1=var1-var2
print("After swapping var1 =\t{}\tvar2 =\t{}\n".format(var1,var2))
