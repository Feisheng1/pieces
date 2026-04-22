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

def geometric_mean(a):
    product = 1
    for ai in a:
        product *= ai
    return product ** (1/len(a))

if __name__ == "__main__":
    K = 2.685452001065306445309714835481795693820382293994462953051022
    a = expand(math.pi, 100)
    print('pi')
    print('geometric mean: ', geometric_mean(a))
    print('relative error: ', math.fabs(geometric_mean(a) - K) / K)
    b = expand(3 ** (1/3), 100)
    print('cube root of 3')
    print('geometric mean: ', geometric_mean(b))
    print('relative error: ', math.fabs(geometric_mean(b) - K) / K)
