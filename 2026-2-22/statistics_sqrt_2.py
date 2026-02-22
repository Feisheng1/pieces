from decimal import Decimal, getcontext
import math
from collections import Counter

def sqrt2_digit_frequency_decimal(n_digits=1000):
    getcontext().prec = n_digits + 10
    sqrt2 = Decimal(2).sqrt()
    sqrt2_str = str(sqrt2)
    decimal_part = sqrt2_str.split('.')[1][:n_digits]
    digit_count = Counter(decimal_part)
    return digit_count, decimal_part

digits_count, decimal_digits = sqrt2_digit_frequency_decimal(1000)

for digit in range(10):
    count = digits_count.get(str(digit), 0)
    percentage = (count / 1000) * 100
    print(f"number {digit}: {count:3d} times ({percentage:.2f}%)")

total = sum(digits_count.values())