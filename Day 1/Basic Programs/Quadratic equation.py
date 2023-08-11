# Quadratic equation format: ax^2+bx+c=0)

a= int(input("Enter the coefficient of x^2:"))
b= int(input("Enter the coefficient of x:"))
c= int(input("Enter the constant:"))

root1=(-b+((b**2)-(4*a*c))**0.5)/(2*a)
root2=(-b-((b**2)-(4*a*c))**0.5)/(2*a)

print("The two roots of the quadratic equation is:", root1, "and", root2)

