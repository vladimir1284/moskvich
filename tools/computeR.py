from numpy import log
T = 65

a = 1.
b = 20000.

def computeT(R):
    R = log(R)
    return 1.0 / (0.001129148 + (0.000234125 + (0.0000000876741 * R**2)) * R) - 273.15


while (b - a > 1):
    V = computeT((a+b)/2)
    Va = computeT(a)
    Vb = computeT(b)

    if (V < T):
        b = (a+b)/2
    else:
        a = (a+b)/2

    print(a,b,Va,V,Vb)

print(a)