def are_valid_triangle_side_lengths(a, b, c):
    '''Test if the provided lengths could form the sides of a triangle'''
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False


def is_right_triangle(a, b, c):
    '''Test if the provided lengths could form the sides of a right triangle'''

    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return True
    else:
        return False

