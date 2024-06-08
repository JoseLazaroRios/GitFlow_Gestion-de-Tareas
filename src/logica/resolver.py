import math

def solve_quadratic(a, b, c):
    """Resolver ecuacion ax^2 + bx + c = 0"""
    if a == 0:
        raise ValueError("El coeficiente 'a' no puede ser cero en una ecuación cuadrática.")

    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None  # No real roots

    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)

    return root1, root2
