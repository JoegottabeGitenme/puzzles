"""
Joseph Hurni

Find a, b, c, d, e, f, and g, all positive integers greater than 1, that satisfy all equations:

a2 × b × c2 × g = 5100

a × b2 × e × f2 = 33462

a × c2 × d3 = 17150

a3 × b3 × c × d × e2 = 914760

in the fastest way possible, using your language of choice.

"""

def dumb_way():
    # this is like big O of (n^7) or something terrible,
    # this will also never finish on a computer made this century with numbers much larger than what's here
    # slap anyone who checks this code in anywhere please
    big_numba = 20
    for a in range(1, big_numba):
        for b in range(1, big_numba):
            for c in range(1, big_numba):
                for d in range(1, big_numba):
                    for e in range(1, big_numba):
                        for f in range(1, big_numba):
                            for g in range(1, big_numba):
                                print(f"trying {[a, b, c, d, e, f, g]}")

                                if (a * a * b * c * c * g == 5100) and (a * b * b * e * f * f == 33462) and (
                                        a * c * c * d * d * d == 17150) and (
                                        a * a * a * b * b * b * c * d * e * e == 914760):
                                    print(f"hey found it {[a, b, c, d, e, f, g]}")
                                    return


# in general with linear algebra stuff, a linear combination of solutions to a problem is also a solution to a problem

# at first I wrote out a little matrix of the powers and the results

#  a |  b  |  c  |  d  |  e  |  f  |  g  |
# ----------------------------------------------
#  2 |  1  |  2  |  0  |  0  |  0  |  1  | 5100
#  1 |  2  |  0  |  0  |  1  |  2  |  0  | 33462
#  1 |  0  |  2  |  3  |  0  |  0  |  0  | 17150
#  3 |  3  |  1  |  1  |  2  |  0  |  0  | 914760
# ------------------------------------------------
#  7 |  6  |  5  |  4  |  3  |  2  |  1  | ????? (add or subtract idk)

# I noticed if I added up the powers they fell into a nice little order, and since adding powers basically translates
# to repeated multiplication (2 ^ 4 * 2 ^ 2) == (2*2*2*2)*(2*2) == (2 ^ 6)
# I figured we could just put all the equations together through multiplication


def prime_factor(n):
    """shamelessly stolen from the internet"""
    # Print the number of two's that divide n
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def smarter_ish():
    """
    a^7 * b^6 * c^5 * d^4 * e^3 * f^2 * g = 5100*33462*17150*914760
    a^7 * b^6 * c^5 * d^4 * e^3 * f^2 * g = 2,677,277,333,530,800,000
    :return:
    """
    # now just need to figure out how to factor this puppy out, and I bet we get some numbers
    prime_list = prime_factor(2677277333530800000)

    # so we have a list of primes, how many times does each appear?
    count_dict = {str(num): prime_list.count(num) for num in prime_list}
    return count_dict


# now that we have our prime factorization, conveniently we are left with multiples of prime numbers that match
# exactly with our above matrix
# {'2': 7, '3': 6, '5': 5, '7': 4, '11': 3, '13': 2, '17': 1}
# {'a': 7, 'b': 6, 'c': 5, 'd': 4, 'e': 3, 'f': 2, 'g': 1}

def confirm_it():
    """not stolen from the internet"""
    a = 2
    b = 3
    c = 5
    d = 7
    e = 11
    f = 13
    g = 17
    first = (a ** 2 * b * c ** 2 * g == 5100)
    second = (a *b**2*e*f**2 == 33462)
    third = (a*c**2*d**3 == 17150)
    fourth = (a**3*b**3*c*d*e**2 == 914760)

    return first and second and third and fourth

# also now that we know all of our prime numbers are less than 20, the really poor implementation above runs in a
# reasonable amount of time (you should still never write code that bad)

"""
trying [2, 3, 5, 7, 11, 13, 13]
trying [2, 3, 5, 7, 11, 13, 14]
trying [2, 3, 5, 7, 11, 13, 15]
trying [2, 3, 5, 7, 11, 13, 16]
trying [2, 3, 5, 7, 11, 13, 17]
hey found it [2, 3, 5, 7, 11, 13, 17] # only took 2,357,111,317 iterations!

Process finished with exit code 0"""


# fun problem, I definitely got a hint from the internet on this one ;), but I feel this was a "recognize that you can
# apply some linear algebra logic here and you'll figure it out" problem. Ran into some issues with the prime
# factorization algorithms (math.sqrt works funny on large numbers, which some algorithms use)

if __name__ == '__main__':
    # dumb_way()
    print(smarter_ish())
    print(confirm_it())
