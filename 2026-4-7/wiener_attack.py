import math

def wiener_attack(N, e):
    def expand_rational(e,N):
        l = []
        while N > 0:
            q = e // N
            l.append(q)
            e, N = N, e - q * N
        return l

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

    cf = expand_rational(e, N)
    convs = convergents(cf)
    for k, d in convs:
        if k == 0:
            continue
        if (e * d - 1) % k != 0:
            continue
        phi = (e * d - 1) // k
        s = N - phi + 1
        D = s*s - 4*N
        if D < 0:
            continue
        sqrt_D = int(math.isqrt(D))
        if sqrt_D * sqrt_D != D:
            continue

        p = (s - sqrt_D) // 2
        q = (s + sqrt_D) // 2
        if p * q == N:
            print(f"p = {p}, q = {q}")
            print(f"Found: d = {d}")
            return d
    return None

N = 17947
e = 11787

d = wiener_attack(N, e)