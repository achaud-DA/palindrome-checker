#!/usr/bin/env python3
"""
Simple tests for palindrome checker functions.
"""

from palindrome_checker import is_palindrome_number, is_palindrome_number_mathematical, find_palindromes_in_range


def test_palindrome_functions():
    """Test both palindrome checking functions."""
    
    # Test cases: (number, expected_result)
    test_cases = [
        (121, True),
        (123, False),
        (1221, True),
        (12321, True),
        (-121, False),
        (0, True),
        (7, True),
        (10, False),
        (1001, True),
        (1234321, True),
        (1234567, False)
    ]
    
    print("Testing palindrome functions...")
    print("=" * 50)
    
    all_passed = True
    
    for num, expected in test_cases:
        # Test string method
        result1 = is_palindrome_number(num)
        # Test mathematical method
        result2 = is_palindrome_number_mathematical(num)
        
        status1 = "PASS" if result1 == expected else "FAIL"
        status2 = "PASS" if result2 == expected else "FAIL"
        
        print(f"Number: {num:8d} | Expected: {str(expected):5s} | String: {str(result1):5s} ({status1}) | Math: {str(result2):5s} ({status2})")
        
        if result1 != expected or result2 != expected:
            all_passed = False
    
    print("=" * 50)
    print(f"Overall result: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    
    return all_passed


def test_range_function():
    """Test the range palindrome finding function."""
    print("\nTesting range function...")
    print("=" * 30)
    
    # Test small range
    result = find_palindromes_in_range(1, 20)
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    print(f"Range 1-20: {result}")
    print(f"Expected:   {expected}")
    print(f"Match: {'YES' if result == expected else 'NO'}")
    
    # Test three-digit palindromes
    result = find_palindromes_in_range(100, 110)
    expected = [101]
    print(f"\nRange 100-110: {result}")
    print(f"Expected:      {expected}")
    print(f"Match: {'YES' if result == expected else 'NO'}")


if __name__ == "__main__":
    test_palindrome_functions()
    test_range_function()
