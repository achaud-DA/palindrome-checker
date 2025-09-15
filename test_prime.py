#!/usr/bin/env python3
"""
Tests for prime number checker functions.
"""

from prime_checker import (
    is_prime, 
    is_prime_optimized, 
    find_primes_in_range, 
    sieve_of_eratosthenes,
    get_prime_factors,
    next_prime,
    is_twin_prime
)


def test_is_prime():
    """Test the basic prime checking function."""
    print("Testing is_prime function...")
    print("=" * 40)
    
    # Test cases: (number, expected_result)
    test_cases = [
        (2, True),      # First prime
        (3, True),      # Small prime
        (4, False),     # First composite
        (5, True),      # Small prime
        (6, False),     # Composite
        (7, True),      # Prime
        (8, False),     # Composite
        (9, False),     # Perfect square
        (10, False),    # Composite
        (11, True),     # Prime
        (17, True),     # Prime
        (25, False),    # Perfect square
        (29, True),     # Prime
        (97, True),     # Larger prime
        (100, False),   # Composite
        (101, True),    # Larger prime
        (1, False),     # Not prime by definition
        (0, False),     # Not prime
        (-5, False),    # Negative number
    ]
    
    all_passed = True
    
    for num, expected in test_cases:
        result = is_prime(num)
        status = "PASS" if result == expected else "FAIL"
        print(f"is_prime({num:3d}) = {str(result):5s} | Expected: {str(expected):5s} | {status}")
        
        if result != expected:
            all_passed = False
    
    print("=" * 40)
    print(f"is_prime tests: {'ALL PASSED' if all_passed else 'SOME FAILED'}")
    return all_passed


def test_is_prime_optimized():
    """Test the optimized prime checking function."""
    print("\nTesting is_prime_optimized function...")
    print("=" * 40)
    
    # Use same test cases as basic function
    test_cases = [
        (2, True), (3, True), (4, False), (5, True), (6, False),
        (7, True), (8, False), (9, False), (10, False), (11, True),
        (17, True), (25, False), (29, True), (97, True), (100, False),
        (101, True), (1, False), (0, False), (-5, False)
    ]
    
    all_passed = True
    
    for num, expected in test_cases:
        result = is_prime_optimized(num)
        status = "PASS" if result == expected else "FAIL"
        print(f"is_prime_optimized({num:3d}) = {str(result):5s} | Expected: {str(expected):5s} | {status}")
        
        if result != expected:
            all_passed = False
    
    print("=" * 40)
    print(f"is_prime_optimized tests: {'ALL PASSED' if all_passed else 'SOME FAILED'}")
    return all_passed


def test_consistency():
    """Test that both prime functions give the same results."""
    print("\nTesting consistency between prime functions...")
    print("=" * 40)
    
    all_consistent = True
    
    for num in range(-5, 101):
        result1 = is_prime(num)
        result2 = is_prime_optimized(num)
        
        if result1 != result2:
            print(f"INCONSISTENCY at {num}: is_prime={result1}, is_prime_optimized={result2}")
            all_consistent = False
    
    print(f"Consistency test: {'PASSED' if all_consistent else 'FAILED'}")
    return all_consistent


def test_find_primes_in_range():
    """Test finding primes in a range."""
    print("\nTesting find_primes_in_range function...")
    print("=" * 40)
    
    # Test cases: (start, end, expected_primes)
    test_cases = [
        (1, 10, [2, 3, 5, 7]),
        (10, 20, [11, 13, 17, 19]),
        (20, 30, [23, 29]),
        (90, 100, [97]),
        (1, 1, []),  # No primes
        (2, 2, [2]),  # Single prime
    ]
    
    all_passed = True
    
    for start, end, expected in test_cases:
        result = find_primes_in_range(start, end)
        status = "PASS" if result == expected else "FAIL"
        print(f"find_primes_in_range({start}, {end}) = {result}")
        print(f"Expected: {expected} | {status}")
        
        if result != expected:
            all_passed = False
        print()
    
    print(f"find_primes_in_range tests: {'ALL PASSED' if all_passed else 'SOME FAILED'}")
    return all_passed


def test_sieve_of_eratosthenes():
    """Test the Sieve of Eratosthenes implementation."""
    print("\nTesting sieve_of_eratosthenes function...")
    print("=" * 40)
    
    # Test cases: (limit, expected_count)
    test_cases = [
        (10, [2, 3, 5, 7]),
        (20, [2, 3, 5, 7, 11, 13, 17, 19]),
        (30, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
        (1, []),
        (2, [2]),
    ]
    
    all_passed = True
    
    for limit, expected in test_cases:
        result = sieve_of_eratosthenes(limit)
        status = "PASS" if result == expected else "FAIL"
        print(f"sieve_of_eratosthenes({limit}) = {result}")
        print(f"Expected: {expected} | {status}")
        
        if result != expected:
            all_passed = False
        print()
    
    print(f"sieve_of_eratosthenes tests: {'ALL PASSED' if all_passed else 'SOME FAILED'}")
    return all_passed


def test_get_prime_factors():
    """Test prime factorization."""
    print("\nTesting get_prime_factors function...")
    print("=" * 40)
    
    # Test cases: (number, expected_factors)
    test_cases = [
        (12, [2, 2, 3]),
        (17, [17]),  # Prime number
        (60, [2, 2, 3, 5]),
        (97, [97]),  # Prime number
        (100, [2, 2, 5, 5]),
        (1, []),
        (2, [2]),
        (9, [3, 3]),
    ]
    
    all_passed = True
    
    for num, expected in test_cases:
        result = get_prime_factors(num)
        status = "PASS" if result == expected else "FAIL"
        print(f"get_prime_factors({num}) = {result}")
        print(f"Expected: {expected} | {status}")
        
        if result != expected:
            all_passed = False
        print()
    
    print(f"get_prime_factors tests: {'ALL PASSED' if all_passed else 'SOME FAILED'}")
    return all_passed


def test_next_prime():
    """Test finding the next prime."""
    print("\nTesting next_prime function...")
    print("=" * 40)
    
    # Test cases: (number, expected_next_prime)
    test_cases = [
        (1, 2),
        (2, 3),
        (3, 5),
        (4, 5),
        (10, 11),
        (13, 17),
        (20, 23),
        (96, 97),
        (100, 101),
    ]
    
    all_passed = True
    
    for num, expected in test_cases:
        result = next_prime(num)
        status = "PASS" if result == expected else "FAIL"
        print(f"next_prime({num:3d}) = {result:3d} | Expected: {expected:3d} | {status}")
        
        if result != expected:
            all_passed = False
    
    print("=" * 40)
    print(f"next_prime tests: {'ALL PASSED' if all_passed else 'SOME FAILED'}")
    return all_passed


def test_is_twin_prime():
    """Test twin prime detection."""
    print("\nTesting is_twin_prime function...")
    print("=" * 40)
    
    # Twin prime pairs: (3,5), (5,7), (11,13), (17,19), (29,31), (41,43)
    test_cases = [
        (3, True),   # Twin with 5
        (5, True),   # Twin with 3 and 7
        (7, True),   # Twin with 5
        (11, True),  # Twin with 13
        (13, True),  # Twin with 11
        (17, True),  # Twin with 19
        (19, True),  # Twin with 17
        (23, False), # Not twin
        (29, True),  # Twin with 31
        (31, True),  # Twin with 29
        (37, False), # Not twin
        (4, False),  # Not prime
        (2, False),  # Prime but not twin (special case)
    ]
    
    all_passed = True
    
    for num, expected in test_cases:
        result = is_twin_prime(num)
        status = "PASS" if result == expected else "FAIL"
        print(f"is_twin_prime({num:2d}) = {str(result):5s} | Expected: {str(expected):5s} | {status}")
        
        if result != expected:
            all_passed = False
    
    print("=" * 40)
    print(f"is_twin_prime tests: {'ALL PASSED' if all_passed else 'SOME FAILED'}")
    return all_passed


def run_all_tests():
    """Run all prime number tests."""
    print("Prime Number Checker - Test Suite")
    print("=" * 50)
    
    results = []
    results.append(test_is_prime())
    results.append(test_is_prime_optimized())
    results.append(test_consistency())
    results.append(test_find_primes_in_range())
    results.append(test_sieve_of_eratosthenes())
    results.append(test_get_prime_factors())
    results.append(test_next_prime())
    results.append(test_is_twin_prime())
    
    print("\n" + "=" * 50)
    print("FINAL RESULTS")
    print("=" * 50)
    
    passed = sum(results)
    total = len(results)
    
    print(f"Tests passed: {passed}/{total}")
    print(f"Overall result: {'ALL TESTS PASSED' if passed == total else 'SOME TESTS FAILED'}")
    
    return passed == total


if __name__ == "__main__":
    run_all_tests()
