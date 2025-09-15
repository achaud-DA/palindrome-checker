# Palindrome Number Checker

A simple Python program to check if a number is a palindrome. A palindrome number reads the same forwards and backwards (e.g., 121, 1331, 7).

## Features

- **Two Implementation Methods:**
  - String-based approach (simple and intuitive)
  - Mathematical approach (without string conversion)
- **Interactive Mode:** Test numbers interactively
- **Range Search:** Find all palindromes within a specified range
- **Comprehensive Testing:** Includes various test cases

## Usage

### Running the Program

```bash
python3 palindrome_checker.py
```

### Using as a Module

```python
from palindrome_checker import is_palindrome_number, find_palindromes_in_range

# Check if a number is palindrome
print(is_palindrome_number(121))  # True
print(is_palindrome_number(123))  # False

# Find palindromes in a range
palindromes = find_palindromes_in_range(1, 100)
print(palindromes)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]
```

## Functions

### `is_palindrome_number(num)`
Checks if a number is a palindrome using string comparison.
- **Parameters:** `num` (int) - The number to check
- **Returns:** `bool` - True if palindrome, False otherwise

### `is_palindrome_number_mathematical(num)`
Checks if a number is a palindrome using mathematical operations only.
- **Parameters:** `num` (int) - The number to check
- **Returns:** `bool` - True if palindrome, False otherwise

### `find_palindromes_in_range(start, end)`
Finds all palindrome numbers within a given range.
- **Parameters:** 
  - `start` (int) - Start of range (inclusive)
  - `end` (int) - End of range (inclusive)
- **Returns:** `list` - List of palindrome numbers

## Examples

```python
# Single number checks
is_palindrome_number(121)    # True
is_palindrome_number(123)    # False
is_palindrome_number(-121)   # False (negative numbers are not palindromes)
is_palindrome_number(7)      # True (single digits are palindromes)

# Range search
find_palindromes_in_range(100, 200)  # [101, 111, 121, 131, 141, 151, 161, 171, 181, 191]
```

## Algorithm Complexity

- **String Method:** O(n) time, O(n) space (where n is the number of digits)
- **Mathematical Method:** O(n) time, O(1) space (where n is the number of digits)

## Requirements

- Python 3.x
- No external dependencies

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/palindrome-checker.git
   cd palindrome-checker
   ```

2. Run the program:
   ```bash
   python3 palindrome_checker.py
   ```

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.
