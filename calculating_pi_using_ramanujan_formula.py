from decimal import Decimal, getcontext
import math
import time

def optimized_ramanujan_pi(precision_digits, verbose=True):

    getcontext().prec = precision_digits + 10
    if verbose:
        start_time = time.time()
        sqrt2 = Decimal(2).sqrt()
        C = (2 * sqrt2) / Decimal(9801)
        total = Decimal(0)
        k = 0
        term = Decimal(1103)
        total += term
    
    while True:
        num_factor = 1
        for j in range(1, 5):
            num_factor *= (4*k + j)
        num_factor *= (1103 + 26390*(k+1))
        denom_factor = ((k+1) ** 4) * (396 ** 4) * (1103 + 26390*k)
        factor = Decimal(num_factor) / Decimal(denom_factor)
        next_term = term * factor
        term = next_term
        total += term
        k += 1
        if abs(term) < Decimal(10) ** (-precision_digits - 2):
            if verbose:
                print(f"last term: {abs(term):.2e}")
            break
        if verbose and k % 10 == 0:
            term_float = float(abs(term))
            if term_float > 0:
                current_precision = -int(math.log10(term_float))
                print(f"  error: {term_float:.2e}, valid: {current_precision}")
            else:
                 print(f"  error: < 10^{-precision_digits}")             
    pi = 1 / (C * total)
    if verbose:
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"time: {elapsed:.2f} s ({elapsed/60:.2f} min)")
    return pi

def calculate_pi_safe(precision_digits, verbose=True):
    pi = optimized_ramanujan_pi(precision_digits, verbose)
    pi_str = str(pi)
    if precision_digits >= 1000:
        digit_1000 = pi_str[1001]
        print(digit_1000)
    return pi

if __name__ == "__main__":
    pi = calculate_pi_safe(1000, verbose=True)
