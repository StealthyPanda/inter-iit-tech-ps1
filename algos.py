from typing import Tuple

#returns angles of arm-sections with respect to x axis, assuming the arm begins at
#basepoint, is single jointed, and the entire arm lies in the same plane.
#basepoint and targetpoint are both cartesian coordinates.
def getangles(sectionlengths : Tuple[float, float], basepoint : Tuple[float, float], targetpoint : Tuple[float, float])->Tuple[float, float]:
    h0, k0 = basepoint[0], basepoint[1]
    h1, k1 = targetpoint[0], targetpoint[1]
    r0, r1 = sectionlengths[0], sectionlengths[1]

    b = 2 * (pow(h0 - h1, 2) - pow(r0, 2) + pow(r1, 2))
    alpha = pow(h0 - h1, 2) + pow(r0, 2) + pow(r1, 2)
    c = pow(alpha, 2) - (4 * pow(r0, 2) * pow(h0 - h1, 2))
    print(b, alpha, c)

    t0, t1 = (
        (-b + pow(pow(b, 2) - (4 * c), 0.5))/2,
        (-b - pow(pow(b, 2) - (4 * c), 0.5))/2
    )
    print(t0, t1)

    if type(t0) == complex : t = t1
    elif type(t1) == complex : t = t0
    else : t = t0 if t0 > 0 else t1

    y0, y1 = (
        k0 + pow(t, 0.5), k0 - pow(t, 0.5)
    )

    y = y0 if y0 > y1 else y1

    x0, x1 = (
        h0 + pow(pow(r0, 2) - pow(y - k0, 2), 0.5),
        h0 - pow(pow(r0, 2) - pow(y - k0, 2), 0.5)
    )

    x0r = pow(x0 - h1, 2) + pow(x0 - k1, 2)
    x1r = pow(x1 - h1, 2) + pow(x1 - k1, 2)

    x = x0 if x0r < x1r else x1

    return (x, y)


if __name__ == '__main__':
    base = (4, 4)
    arms = (1, 3.6)
    target = (1, 1)

    print(getangles(arms, base, target))