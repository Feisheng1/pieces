import math

def expand_sqrt(D):
    s = int(math.sqrt(D))
    if s * s == D:
        return s, []
    m = 0
    d = 1
    a = s
    a0 = a
    a_cycle = []
    states = {}
    while True:
        m = d * a - m
        d = (D - m * m) // d
        a = (s + m) // d
        if (m, d) in states:
            cycle_start = states[(m, d)]
            return a0, a_cycle[cycle_start:]
        states[(m, d)] = len(a_cycle)
        a_cycle.append(a)


def solve(D):
    a0, cycle = expand_sqrt(D)
    p0, p1 = 1, a0
    q0, q1 = 0, 1
    if p1 * p1 - D * q1 * q1 == 1:
        return p1, q1
    cycle_length = len(cycle)
    i = 0
    while True:
        a = cycle[i % cycle_length]
        p2 = a * p1 + p0
        q2 = a * q1 + q0
        if p2 * p2 - D * q2 * q2 == 1:
            return p2, q2
        p0, p1 = p1, p2
        q0, q1 = q1, q2
        i += 1

if __name__ == "__main__":
    print(solve(46))
    print(solve(61))
