"""
Write a function, is_prime, that takes an integer and returns True if
the number is prime and False if the number is not prime.
"""
def is_prime(n):
    count=0
    if n==0 or n==1:
        return f"Neither Prime Nor Composite"
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False
if __name__ == "__main__":
    inputNo = int(input('Enter any no'))
    print(is_prime(inputNo))