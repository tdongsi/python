
import fractions
import random


def decompose(num):
    """ Decompose num = 2**exp * d where d is odd.

    :param num: the input number.
    :return: (exp, d) where num = 2**exp * d
    """
    exp = 0
    while num & 1 == 0:  # check num % 2 == 0 but probably faster
        num >>= 1
        exp += 1
    return exp, num


def is_pseudo_prime(prime, trial=10):
    """ Rabin Miller test of primality.

    :param prime: the input number.
    :param trial: Number of Rabin-Miller trial.
    :return: True if all trials passed, False if not.
    """

    # small primes < 100
    SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                    43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    def rabin_miller_trial(prime, num):
        """ Check if prime pass the Rabin-Miller trial.

        :param prime: a prospective prime.
        :param num: a random "witness" of primality.

        :return: True if composite, False if probably prime.
        """
        num = pow(num, remainder, prime)

        # For first iteration, 1 or -1 remainder implies prime
        if num == 1 or num == prime - 1:
            return False

        # For next iterations, -1 implies prime, 1 implies composite
        for _ in xrange(exponent):
            num = pow(num, 2, prime)
            if num == prime - 1:
                return False

        return True

    # Labor saving steps
    if prime < 2:
        return False
    for p in SMALL_PRIMES:
        if p * p > prime:
            return True
        if prime % p == 0:
            return False

    # Starting Rabin-Miller algorithm
    exponent, remainder = decompose(prime - 1)

    for _ in xrange(trial):
        num = random.randint(2, prime - 2)
        if rabin_miller_trial(prime, num):
            return False

    return True


def find_factor(prime, trial=100):
    """ Modify Rabin Miller test of primality to find factor of composite.

    :param prime: the input number.
    :param trial: Number of Rabin-Miller trials.
    :return: 1 if prime (all trials passed), > 1 if composite.
    """

    # small primes < 100
    SMALL_PRIMES = [ 2,   3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,  41,
                  43,  47,  53,  59,  61,  67,  71,  73,  79,  83,  89,  97, 101,
                 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
                 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239,
                 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
                 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
                 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
                 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
                 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643,
                 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
                 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823,
                 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
                 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    def rabin_miller_trial(prime, num):
        """ Find factor based on the Rabin-Miller trial.

        :param prime: a prospective prime.
        :param num: a random "witness" of primality.

        :return: > 1 if composite, 1 if probably prime.
        """
        num = pow(num, remainder, prime)

        # For first iteration, 1 or -1 remainder implies prime
        if num == 1 or num == prime - 1:
            return 1
        else:
            gcd = fractions.gcd(num-1, prime)
            if gcd > 1:
                return gcd

        # For next iterations, -1 implies prime, 1 implies composite
        for _ in xrange(exponent):
            num = pow(num, 2, prime)
            if num == prime - 1:
                return 1
            else:
                gcd = fractions.gcd(num-1, prime)
                if gcd > 1:
                    return gcd

        # It is a composite, but could not find a factor
        return -1

    # Labor saving steps
    if prime < 2:
        raise ValueError("Unexpected input")
    for p in SMALL_PRIMES:
        if p * p > prime:
            return 1
        if prime % p == 0:
            return p

    # Starting Rabin-Miller algorithm
    exponent, remainder = decompose(prime - 1)

    for _ in xrange(trial):
        num = random.randint(2, prime - 2)
        factor = rabin_miller_trial(prime, num)
        if factor > 1:
            return factor

    return 1
