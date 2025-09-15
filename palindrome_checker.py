#!/usr/bin/env python3
"""
Palindrome Number Checker

This module provides functions to check if a number is a palindrome.
A palindrome number reads the same forwards and backwards.
"""


def is_palindrome_number(num):
    """
    Check if a number is a palindrome.
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if the number is a palindrome, False otherwise
        
    Examples:
        >>> is_palindrome_number(121)
        True
        >>> is_palindrome_number(123)
        False
        >>> is_palindrome_number(-121)
        False
    """
    # Negative numbers are not palindromes
    if num < 0:
        return False
    
    # Convert to string and check if it reads the same forwards and backwards
    str_num = str(num)
    return str_num == str_num[::-1]


def is_palindrome_number_mathematical(num):
    """
    Check if a number is a palindrome using mathematical approach (without string conversion).
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if the number is a palindrome, False otherwise
    """
    # Negative numbers are not palindromes
    if num < 0:
        return False
    
    # Single digit numbers are palindromes
    if num < 10:
        return True
    
    original = num
    reversed_num = 0
    
    # Reverse the number mathematically
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    
    return original == reversed_num


def find_palindromes_in_range(start, end):
    """
    Find all palindrome numbers in a given range.
    
    Args:
        start (int): Start of the range (inclusive)
        end (int): End of the range (inclusive)
        
    Returns:
        list: List of palindrome numbers in the range
    """
    palindromes = []
    for num in range(start, end + 1):
        if is_palindrome_number(num):
            palindromes.append(num)
    return palindromes


def main():
    """Main function to demonstrate palindrome checking."""
    print("Palindrome Number Checker")
    print("=" * 25)
    
    # Test some numbers
    test_numbers = [121, 123, 1221, 12321, -121, 0, 7, 1001]
    
    print("\nTesting individual numbers:")
    for num in test_numbers:
        result = is_palindrome_number(num)
        print(f"{num:6d} -> {'Palindrome' if result else 'Not palindrome'}")
    
    print("\nTesting mathematical approach:")
    for num in test_numbers:
        result = is_palindrome_number_mathematical(num)
        print(f"{num:6d} -> {'Palindrome' if result else 'Not palindrome'}")
    
    # Find palindromes in a range
    print(f"\nPalindromes between 1 and 100:")
    palindromes = find_palindromes_in_range(1, 100)
    print(palindromes)
    
    print(f"\nPalindromes between 100 and 1000:")
    palindromes = find_palindromes_in_range(100, 1000)
    print(palindromes)
    
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
            result = is_palindrome_number(num)
            print(f"{num} is {'a palindrome' if result else 'not a palindrome'}")
            
        except ValueError:
            print("Please enter a valid integer or 'quit' to exit.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
