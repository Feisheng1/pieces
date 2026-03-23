def expand_rational(a,b):
    l = []
    while b != 0:
        q = a // b
        l.append(q)
        a, b = b, a - q * b
    return l

def solve(a,b):
    g = max(a,b)
    m = min(a,b)
    p_n2,p_n1 = 0,1
    q_n2,q_n1 = 1,0
    expanded = expand_rational(g,m)
    for i in range(len(expanded)-1):
        p_i = expanded[i] * p_n1 + p_n2
        q_i = expanded[i] * q_n1 + q_n2
        p_n2,p_n1 = p_n1,p_i
        q_n2,q_n1 = q_n1,q_i

    r1, r2 = q_n1, p_n1
    if a*q_n1 - b*p_n1 == -1 and g == a:
        r1, r2 = -q_n1, -p_n1
    elif a*p_n1 - b*q_n1 == -1 and g == b:
        r1, r2 = -p_n1, -q_n1
    elif a*p_n1 - b*q_n1 == 1 and g == b:
        r1, r2 = p_n1, q_n1

    return r1, r2

if __name__ == "__main__":
    print(solve(7654321,9876543))
