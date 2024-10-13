#to check whether an integer in prime number or not

def is_prime(num):
    if num <= 1:  # 0 and 1 are not prime numbers
        return False
    for i in range(2, int(num**0.5) + 1):  # Check up to the square root of the number
        if num % i == 0:
            return False
    return True

# Get user input
number = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
