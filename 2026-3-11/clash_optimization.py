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

def clash(Q):
    best_p, best_q = 0, 1
    min_error = float('inf')
    
    for q in range(1, Q + 1):
        p = round(math.pi * q)
        error = abs(math.pi - p / q)
        if error < min_error:
            min_error = error
            best_p, best_q = p, q
    return best_p, best_q

def main():
    Q_list = [10, 50, 100, 500, 1000]
    for Q in Q_list:
        p, q = clash(Q)
        print(f"{p}/{q}")

if __name__ == "__main__":
    cf = expand(10)
    main()