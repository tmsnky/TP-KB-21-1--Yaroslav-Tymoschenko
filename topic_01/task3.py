def quadratic_discriminant(a, b, c):
    discriminant = b**2 - 4*a*c
    return discriminant


a_coefficient = 2
b_coefficient = -4
c_coefficient = 1

discriminant_value = quadratic_discriminant(a_coefficient, b_coefficient, c_coefficient)
print("Discriminant:", discriminant_value)