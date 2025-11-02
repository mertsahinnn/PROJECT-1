def triangle_membership(x, a, b, c):
    """
    Calculate the triangular membership value for a given input x.

    Parameters:
    x (float): The input value.
    a (float): The left vertex of the triangle.
    b (float): The peak vertex of the triangle.
    c (float): The right vertex of the triangle.

    Returns:
    float: The membership value ranging from 0 to 1.
    """
    if a < x < b:
        return (x - a) / (b - a)
    elif b <= x < c:
        return (c - x) / (c - b)
    elif x == b:
        return 1.0
    else:
        return 0.0
    

def trapezoidal_membership(x, a, b, c, d):
    """
    Calculate the trapezoidal membership value for a given input x.

    Parameters:
    x (float): The input value.
    a (float): The left foot of the trapezoid.
    b (float): The left shoulder of the trapezoid.
    c (float): The right shoulder of the trapezoid.
    d (float): The right foot of the trapezoid.

    Returns:
    float: The membership value ranging from 0 to 1.
    """
    if a < x < b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return 1.0
    elif c < x < d:
        return (d - x) / (d - c)
    else:
        return 0.0