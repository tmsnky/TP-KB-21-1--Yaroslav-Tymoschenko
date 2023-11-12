def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + (discriminant)**0.5) / (2*a)
        root2 = (-b - (discriminant)**0.5) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        return "No real roots"


a = 1
b = -3
c = 2


roots = quadratic_roots(a, b, c)
print("Roots:", roots)
