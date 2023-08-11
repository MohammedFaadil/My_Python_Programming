a=int(input("Enter the side 1 of the triangle:"))
b=int(input("Enter the side 2 of the triangle:"))
c=int(input("Enter the side 3 of the triangle:"))
sp= (a+b+c)*0.5
area = (sp*(sp-a)*(sp-b)*(sp-c))**0.5
print("The area of the triangle is:", area)
