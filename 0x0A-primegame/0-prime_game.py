#!/usr/bin/python3

def sieve_of_eratosthenes(max_num):
    """ Generate a list of primes up to max_num using the Sieve of Eratosthenes. """
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(max_num + 1) if is_prime[p]]

def isWinner(x, nums):
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    def play_game(n):
        """ Simulate the game for a given n and return the winner. """
        removed = [False] * (n + 1)
        
        turn = 0  # 0 for Maria, 1 for Ben
        remaining_primes = primes
        
        for prime in remaining_primes:
            if prime > n:
                break
            if not removed[prime]:
                for multiple in range(prime, n + 1, prime):
                    removed[multiple] = True
                turn = 1 - turn
        return "Ben" if turn == 0 else "Maria"
    
    winner_count = {"Maria": 0, "Ben": 0}
    
    for n in nums:
        winner = play_game(n)
        winner_count[winner] += 1
    
    if winner_count["Maria"] > winner_count["Ben"]:
        return "Maria"
    elif winner_count["Ben"] > winner_count["Maria"]:
        return "Ben"
    else:
        return None
