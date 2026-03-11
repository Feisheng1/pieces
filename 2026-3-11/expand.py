import math

def expand(x, N):
    a = [0] * N
    for i in range(N):
        a[i] = int(x)
        if x-a[i] == 0:
            break
        x = 1/(x-a[i])
    return a

if __name__ == "__main__":
    a1 = expand(math.sqrt(7), 100)
    a2 = expand(math.e - 1, 100)
    a3 = expand(math.pi, 10)
    print(a1)
    print(a2)
    print(a3)