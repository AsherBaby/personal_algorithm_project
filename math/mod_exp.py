"""
Efficient algorithm for modular exponentiation
"""

def mod_exp(base, exp, mod):
    """
    >>> mod_exp(3, 644, 645)
    36
    """
    b = bin(exp)[2:]
    x = 1
    power = base % mod  # next power
    for i in range(len(b)-1, -1, -1):
        if b[i] == '1':
            x = (x*power) % mod
        power = pow(power, 2) % mod
    return x
