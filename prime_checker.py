#!/usr/bin/env python3
"""
Prime Number Checker

This module provides functions to check if a number is prime and find prime numbers.
A prime number is a natural number greater than 1 that has no positive divisors 
other than 1 and itself.
"""

import math


def is_prime(num):
    """
    Check if a number is prime using trial division.
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
        
    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
        >>> is_prime(17)
        True
        >>> is_prime(-5)
        False
    """
    # Numbers less than 2 are not prime
    if num < 2:
        return False
    
    # 2 is the only even prime number
    if num == 2:
        return True
    
    # Even numbers greater than 2 are not prime
    if num % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(num)
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    
    return True


def is_prime_optimized(num):
    """
    Optimized prime checking using 6k±1 optimization.
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
    """
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    # Check for divisors of the form 6k±1
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    
    return True


def find_primes_in_range(start, end):
    """
    Find all prime numbers in a given range.
    
    Args:
        start (int): Start of the range (inclusive)
        end (int): End of the range (inclusive)
        
    Returns:
        list: List of prime numbers in the range
    """
    primes = []
    for num in range(max(2, start), end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def sieve_of_eratosthenes(limit):
    """
    Find all prime numbers up to a given limit using Sieve of Eratosthenes.
    This is more efficient for finding many primes.
    
    Args:
        limit (int): Upper limit to find primes up to
        
    Returns:
        list: List of prime numbers up to the limit
    """
    if limit < 2:
        return []
    
    # Create a boolean array and initialize all entries as True
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime
    
    p = 2
    while p * p <= limit:
        if sieve[p]:
            # Mark all multiples of p as not prime
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
        p += 1
    
    # Collect all prime numbers
    return [i for i in range(2, limit + 1) if sieve[i]]


def get_prime_factors(num):
    """
    Get the prime factorization of a number.
    
    Args:
        num (int): The number to factorize
        
    Returns:
        list: List of prime factors
    """
    if num < 2:
        return []
    
    factors = []
    
    # Check for factor 2
    while num % 2 == 0:
        factors.append(2)
        num //= 2
    
    # Check for odd factors
    i = 3
    while i * i <= num:
        while num % i == 0:
            factors.append(i)
            num //= i
        i += 2
    
    # If num is still greater than 1, it's a prime factor
    if num > 1:
        factors.append(num)
    
    return factors


def next_prime(num):
    """
    Find the next prime number after a given number.
    
    Args:
        num (int): The number to find the next prime after
        
    Returns:
        int: The next prime number
    """
    candidate = num + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate


def is_twin_prime(num):
    """
    Check if a number is part of a twin prime pair.
    Twin primes are pairs of primes that differ by 2.
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if the number is part of a twin prime pair
    """
    if not is_prime(num):
        return False
    
    return is_prime(num - 2) or is_prime(num + 2)


def main():
    """Main function to demonstrate prime number functionality."""
    print("Prime Number Checker")
    print("=" * 20)
    
    # Test some numbers
    test_numbers = [2, 3, 4, 5, 17, 25, 29, 97, 100, 101]
    
    print("\nTesting individual numbers:")
    for num in test_numbers:
        result = is_prime(num)
        optimized_result = is_prime_optimized(num)
        print(f"{num:3d} -> {'Prime' if result else 'Not prime'} | Optimized: {'Prime' if optimized_result else 'Not prime'}")
    
    # Find primes in a range
    print(f"\nPrimes between 1 and 50:")
    primes = find_primes_in_range(1, 50)
    print(primes)
    
    # Sieve of Eratosthenes
    print(f"\nPrimes up to 30 (using Sieve):")
    sieve_primes = sieve_of_eratosthenes(30)
    print(sieve_primes)
    
    # Prime factorization
    print(f"\nPrime factorization examples:")
    test_factors = [12, 17, 60, 97]
    for num in test_factors:
        factors = get_prime_factors(num)
        print(f"{num} = {' × '.join(map(str, factors))}")
    
    # Twin primes
    print(f"\nTwin primes up to 30:")
    twin_primes = [p for p in sieve_primes if is_twin_prime(p)]
    print(twin_primes)
    
    # Interactive mode
    print("\n" + "=" * 40)
    print("Interactive Mode - Enter numbers to check")
    print("Type 'quit' to exit")
    
    while True:
        try:
            user_input = input("\nEnter a number: ").strip()
            if user_input.lower() == 'quit':
                break
            
            num = int(user_input)
            result = is_prime(num)
            print(f"{num} is {'prime' if result else 'not prime'}")
            
            if result:
                print(f"Next prime after {num}: {next_prime(num)}")
                if is_twin_prime(num):
                    print(f"{num} is part of a twin prime pair!")
            else:
                factors = get_prime_factors(num)
                if len(factors) > 1:
                    print(f"Prime factors: {factors}")
                
        except ValueError:
            print("Please enter a valid integer or 'quit' to exit.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
