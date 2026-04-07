import math

def expand(x, N):
    a = [0] * N
    for i in range(N):
        a[i] = int(x)
        if x-a[i] == 0:
            break
        x = 1/(x-a[i])
    return a

def convergents(a):
    convergents = []
    p_prev2, q_prev2 = 1, 0
    p_prev1, q_prev1 = a[0], 1
    convergents.append((p_prev1, q_prev1))

    for ai in a[1:]:
        p = ai * p_prev1 + p_prev2
        q = ai * q_prev1 + q_prev2
        convergents.append((p, q))
        p_prev2, p_prev1 = p_prev1, p
        q_prev2, q_prev1 = q_prev1, q
    
    return convergents

def irrational_exponents(a):
    mu = []
    for p, q in a:
        if q == 1:
            continue
        mu.append(- math.log(math.fabs(math.pi - p/q)) / math.log(q))
    r = 0
    for e in mu:
        if e > r:
            r = e
    return r

if __name__ == "__main__":
    a = expand(math.pi, 10)
    b = convergents(a)
    print(b)
    p, q = b[-1]
    print(p/q)
    b = b[5:10]
    print(irrational_exponents(b))