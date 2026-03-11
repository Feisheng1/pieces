import math

def expand(max_terms=50):
    x = math.pi
    a = []
    for _ in range(max_terms):
        ai = int(x)
        a.append(ai)
        if x - ai == 0:
            break
        x = 1 / (x - ai)
    return a

def optimize(Q):
    a = expand(30)

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
        if q > 1000:
            break
    
    candidates = []
    
    for i in range(len(convergents) - 1):
        p1, q1 = convergents[i]
        if q1 <= Q:
            candidates.append((p1, q1))

    p_last, q_last = convergents[-1]
    if q_last <= Q:
        candidates.append((p_last, q_last))

    candidates = list(set(candidates))
    best_p, best_q = min(candidates, key=lambda x: abs(math.pi - x[0] / x[1]))
    
    return best_p, best_q

def main():
    Q_list = [10, 50, 100, 500, 1000]
    
    for Q in Q_list:
        p, q = optimize(Q)
        print(f"{p}/{q}")

if __name__ == "__main__":
    main()