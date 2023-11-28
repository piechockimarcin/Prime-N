#Marcin Piechocki Prime Number HW
#Prime number checker
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

#Print prime number value set by "N"
def print_primes(N):
    count = 0
    num = 2
    while count < N:
        if is_prime(num):
            print(num, end=" ")
            count += 1
        num += 1
        if count >= N:
            break  # Stop when N integers displayed

#User input for "N"
N = int(input("Enter the value of N: "))
print_primes(N)
