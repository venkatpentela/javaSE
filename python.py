import math

# Input coefficients
a = float(input("Enter the coefficient of 'a': "))
b = float(input("Enter the coefficient of 'b': "))
c = float(input("Enter the coefficient of 'c': "))

# Calculate the discriminant
d = b**2 - 4*a*c

# Check the type of roots based on the discriminant
if d > 0:
    e = (-b + math.sqrt(d)) / (2 * a)
    f = (-b - math.sqrt(d)) / (2 * a)
    print("Roots are real and distinct.")
    print("e =", e)
    print("f =", f)
elif d == 0:
    root = -b / (2 * a)
    print("Root =", root)
    print("Roots are equal.")
else:
    rp = -b / (2 * a)
    img = math.sqrt(-d) / (2 * a)
    print("Roots are complex and distinct.")
    print(f"e = {rp}+{img}i")
    print(f"f = {rp}-{img}i")

