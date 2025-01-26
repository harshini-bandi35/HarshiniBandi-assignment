def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def primes_between(a, b):
    return [num for num in range(a, b + 1) if is_prime(num)]

# Input from user
a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))

# Output the prime numbers
result = primes_between(a, b)
print(f"Prime numbers between {a} and {b}: {result}")