from typing import Tuple
from math import atan

def getangles(sectionlengths : Tuple[float, float], basepoint : Tuple[float, float], targetpoint : Tuple[float, float])->Tuple[float, float]:
    """
    returns angles of arm-sections with respect to x axis, assuming the arm begins at
    basepoint, is single jointed, and the entire arm lies in the same plane.
    basepoint and targetpoint are both cartesian coordinates.
    """
    
    h0, k0 = basepoint[0], basepoint[1]
    h1, k1 = targetpoint[0], targetpoint[1]
    r0, r1 = sectionlengths[0], sectionlengths[1]

    a = pow(k0 - k1, 2) + pow(h0 - h1, 2)

    beta = pow(k1, 2) - pow(k0, 2) + pow(r0, 2) - pow(r1, 2) + pow(h0 - h1, 2)

    b = (beta * (k0 - k1)) - (2 * k0 * pow(h0 - h1, 2))

    c = (pow(beta, 2)/4) + (pow(h0 - h1, 2) * (pow(k0, 2) - pow(r0, 2)))

    d = pow(b, 2) - (4 * a * c)

    y0, y1 = (
        (-b + pow(d, 0.5))/(2*a),
        (-b - pow(d, 0.5))/(2*a)
    )

    y = y0 if y0 > y1 else y1

    x0, x1 = (
        h0 + pow( pow(r0, 2) - pow(y - k0, 2) , 0.5),
        h0 - pow( pow(r0, 2) - pow(y - k0, 2) , 0.5)
    )

    # print("xs",x0,x1)

    z0 = pow(pow(x0 - h1, 2) + pow(y - k1, 2) - pow(r1, 2), 2)
    z1 = pow(pow(x1 - h1, 2) + pow(y - k1, 2) - pow(r1, 2), 2)

    # print("zs",z0, z1)

    x = x0 if z0 < z1 else x1

    # print(f"Intersection point : {(x, y)}")

    theta0 = atan((y - k0)/(x - h0))
    theta1 = atan((k1 - y)/(h1 - x))

    return (theta0, theta1)


if __name__ == '__main__':
    base = (1, 2)
    arms = (1, 2.2)
    target = (3.6, 1.51)

    print(getangles(arms, base, target))