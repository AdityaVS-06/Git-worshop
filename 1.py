import math

print("Enter the coefficients of the quadratic equation (ax² + bx + c = 0):")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = b**2 - 4*a*c
if D > 0:
        r1 = (-b + math.sqrt(D)) / (2 * a)
        r2 = (-b - math.sqrt(D)) / (2 * a)
        print("The roots are real and distinct:")
        print("X1=", r1)
        print("X2 =", r2)
elif D == 0:
        r = -b / (2 * a)
        print("The roots are real and equal:")
        print("X1=X2=", r)

else: 
        print("sucess")

