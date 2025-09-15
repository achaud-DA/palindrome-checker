# Number Theory Toolkit

A comprehensive Python toolkit for number theory operations including palindrome detection and prime number analysis. This repository contains utilities for checking palindromes, finding prime numbers, and performing various number theory calculations.

## Features

### Palindrome Number Checker
- **Two Implementation Methods:**
  - String-based approach (simple and intuitive)
  - Mathematical approach (without string conversion)
- **Interactive Mode:** Test numbers interactively
- **Range Search:** Find all palindromes within a specified range

### Prime Number Checker
- **Multiple Prime Detection Algorithms:**
  - Basic trial division method
  - Optimized 6k±1 algorithm
  - Sieve of Eratosthenes for bulk prime finding
- **Prime Analysis Tools:**
  - Prime factorization
  - Twin prime detection
  - Next prime finder
- **Range Operations:** Find all primes within specified ranges
- **Interactive Testing:** Test numbers for primality with detailed analysis

### General Features
- **Comprehensive Testing:** Extensive test suites for all functions
- **Performance Optimizations:** Multiple algorithms for different use cases
- **Educational Examples:** Clear demonstrations of number theory concepts

## Usage

### Running the Programs

**Palindrome Checker:**
```bash
python3 palindrome_checker.py
```

**Prime Number Checker:**
```bash
python3 prime_checker.py
```

**Running Tests:**
```bash
python3 test_palindrome.py
python3 test_prime.py
```

### Using as a Module

**Palindrome Operations:**
```python
from palindrome_checker import is_palindrome_number, find_palindromes_in_range

# Check if a number is palindrome
print(is_palindrome_number(121))  # True
print(is_palindrome_number(123))  # False

# Find palindromes in a range
palindromes = find_palindromes_in_range(1, 100)
print(palindromes)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]
```

**Prime Number Operations:**
```python
from prime_checker import is_prime, find_primes_in_range, sieve_of_eratosthenes, get_prime_factors

# Check if a number is prime
print(is_prime(17))  # True
print(is_prime(18))  # False

# Find primes in a range
primes = find_primes_in_range(10, 30)
print(primes)  # [11, 13, 17, 19, 23, 29]

# Use Sieve of Eratosthenes for efficiency with large ranges
primes_up_to_100 = sieve_of_eratosthenes(100)
print(len(primes_up_to_100))  # 25 primes up to 100

# Get prime factorization
factors = get_prime_factors(60)
print(factors)  # [2, 2, 3, 5]
```

## Functions

### Palindrome Functions

#### `is_palindrome_number(num)`
Checks if a number is a palindrome using string comparison.
- **Parameters:** `num` (int) - The number to check
- **Returns:** `bool` - True if palindrome, False otherwise

#### `is_palindrome_number_mathematical(num)`
Checks if a number is a palindrome using mathematical operations only.
- **Parameters:** `num` (int) - The number to check
- **Returns:** `bool` - True if palindrome, False otherwise

#### `find_palindromes_in_range(start, end)`
Finds all palindrome numbers within a given range.
- **Parameters:** 
  - `start` (int) - Start of range (inclusive)
  - `end` (int) - End of range (inclusive)
- **Returns:** `list` - List of palindrome numbers

### Prime Number Functions

#### `is_prime(num)`
Checks if a number is prime using trial division.
- **Parameters:** `num` (int) - The number to check
- **Returns:** `bool` - True if prime, False otherwise

#### `is_prime_optimized(num)`
Optimized prime checking using 6k±1 optimization.
- **Parameters:** `num` (int) - The number to check
- **Returns:** `bool` - True if prime, False otherwise

#### `find_primes_in_range(start, end)`
Finds all prime numbers within a given range.
- **Parameters:**
  - `start` (int) - Start of range (inclusive)
  - `end` (int) - End of range (inclusive)
- **Returns:** `list` - List of prime numbers

#### `sieve_of_eratosthenes(limit)`
Finds all primes up to a limit using the Sieve of Eratosthenes algorithm.
- **Parameters:** `limit` (int) - Upper limit to find primes up to
- **Returns:** `list` - List of prime numbers up to the limit

#### `get_prime_factors(num)`
Gets the prime factorization of a number.
- **Parameters:** `num` (int) - The number to factorize
- **Returns:** `list` - List of prime factors

#### `next_prime(num)`
Finds the next prime number after a given number.
- **Parameters:** `num` (int) - The number to find the next prime after
- **Returns:** `int` - The next prime number

#### `is_twin_prime(num)`
Checks if a number is part of a twin prime pair.
- **Parameters:** `num` (int) - The number to check
- **Returns:** `bool` - True if part of a twin prime pair

## Examples

### Palindrome Examples
```python
# Single number checks
is_palindrome_number(121)    # True
is_palindrome_number(123)    # False
is_palindrome_number(-121)   # False (negative numbers are not palindromes)
is_palindrome_number(7)      # True (single digits are palindromes)

# Range search
find_palindromes_in_range(100, 200)  # [101, 111, 121, 131, 141, 151, 161, 171, 181, 191]
```

### Prime Number Examples
```python
# Prime checking
is_prime(17)                 # True
is_prime(18)                 # False
is_prime(97)                 # True

# Finding primes in ranges
find_primes_in_range(10, 30) # [11, 13, 17, 19, 23, 29]
sieve_of_eratosthenes(20)    # [2, 3, 5, 7, 11, 13, 17, 19]

# Prime analysis
get_prime_factors(60)        # [2, 2, 3, 5] (60 = 2² × 3 × 5)
next_prime(10)               # 11
is_twin_prime(17)            # True (17 and 19 are twin primes)
```

## Algorithm Complexity

### Palindrome Algorithms
- **String Method:** O(n) time, O(n) space (where n is the number of digits)
- **Mathematical Method:** O(n) time, O(1) space (where n is the number of digits)

### Prime Number Algorithms
- **Basic Prime Check:** O(√n) time, O(1) space
- **Optimized Prime Check:** O(√n) time, O(1) space (with 6k±1 optimization)
- **Sieve of Eratosthenes:** O(n log log n) time, O(n) space
- **Prime Factorization:** O(√n) time, O(log n) space

## Requirements

- Python 3.x
- No external dependencies

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/achaud-DA/palindrome-checker.git
   cd palindrome-checker
   ```

2. Run the programs:
   ```bash
   # Palindrome checker
   python3 palindrome_checker.py
   
   # Prime number checker
   python3 prime_checker.py
   
   # Run tests
   python3 test_palindrome.py
   python3 test_prime.py
   ```

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.
