import math

def gause_map(x):
    return 1/x - int(1/x)

def tracing_pi(x, x_p, n):
    for i in range(n):
        x.append(gause_map(x[-1]))
        x_p.append(gause_map(x_p[-1]))

def find_n(x, x_p):
    for i in range(len(x)):
        if abs(x[i] - x_p[i])>0.5:
            return i

if __name__ == "__main__":
    x = []
    x.append(math.pi-3)
    x_p = []
    x_p.append(x[0]+10**(-10))
    tracing_pi(x, x_p, 10)

    print('x:', x)
    print('x_p:', x_p)
    print('n:', find_n(x, x_p))
