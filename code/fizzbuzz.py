# # The task

# Write a program that prints the numbers from 1 to 100. If it’s a multiple of 3, it should print “Fizz”. If it’s a multiple of 5, it should print “Buzz”. If it’s a multiple of 3 and 5, it should print “Fizz Buzz”.

# this is the code we came up during the workshop

UPPER_RANGE = 100

for n in range(1, UPPER_RANGE + 1):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)


# this was to show it with a function, and some checks
def fizzbuzz(n):
    if n % (5 * 3) == 0:
        return 'FizzBuzz'
    if n % 3 == 0:
        return 'Fizz'
    if n % 5 == 0:
        return 'Buzz'
    return n


assert fizzbuzz(3) == "Fizz"
assert fizzbuzz(5) == "Buzz"
assert fizzbuzz(15) == "FizzBuzz"
assert fizzbuzz(4) == 4


# let's use a function
def repeat_fizzbuzz(n):
    for i in range(1, n+1):
        print(fizzbuzz(i))


repeat_fizzbuzz(100)
