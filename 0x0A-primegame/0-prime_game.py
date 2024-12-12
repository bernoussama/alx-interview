#!/usr/bin/python3
"""Prime Game Module
"""


def isWinner(x, nums):
    """Determine the winner of the prime game."""

    def sieve_count_primes(max_n):
        """Generate a list of prime counts up to max_n."""
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False
        prime_count = [0] * (max_n + 1)

        for i in range(2, max_n + 1):
            if is_prime[i]:
                for j in range(i * i, max_n + 1, i):
                    is_prime[j] = False
            prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

        return prime_count

    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    prime_count = sieve_count_primes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
