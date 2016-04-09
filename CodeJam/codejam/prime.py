
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

    exponent, remainder = decompose(prime - 1)

    for _ in xrange(trial):
        num = random.randint(2, prime - 2)
        if rabin_miller_trial(prime, num):
            return False

    return True
