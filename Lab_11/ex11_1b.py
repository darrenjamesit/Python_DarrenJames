print('Please choose 3 values for the sides of a triangle:')

a = int(input('Length of side A: '))
b = int(input('Length of side B: '))
c = int(input('Length of side C: '))



def triangle(a, b, c):
    """Function for defining a traingle.
       Parameters
       ----------
       a : int
       Integer length of a side.
       b : int
       Integer length of a side.
       c : int
       Integer length of a side.
       Returns
       ----------
       None:
       Simply prints a statement, does not return anything.
       Example usage:
       >>> triangle(a=3, b=3, c=3)
       Triunghiul este echilateral.
       >>> triangle(a=4, b=4, c=3)
       Triunghiul este isoscel.
       >>> triangle(a=3, b=4, c=5)
       Triunghiul este dreptunghic.
       """
    d = a ** 2
    e = b ** 2
    f = c ** 2
    if a == b == c:
        print('Triunghiul este echilateral.')
    elif a == b or b == c or a == c:
        print('Triunghiul este isoscel.')
    elif (d + e) == f or (e + f) == d or (d + f) == e:
        print('Triunghiul este dreptunghic.')
    else:
        print('Triunghiul este oarecare.')


if __name__ == '__main__':
    from doctest import testmod
    testmod()
    testmod(verbose=True)
