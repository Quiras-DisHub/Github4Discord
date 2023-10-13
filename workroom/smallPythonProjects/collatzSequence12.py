import sys, time

print("""Collatz Sequence
      
      The Collatzsequence is a sequence of numbers produced from a starting
      number n, following three rules:
      
      1) If n is even, the next number n is n / 2.
      2) If n is odd, the next number n i n * 3 + 1.
      3) If n is 1, stop. Otherwise, repeat
      
      It is generally thought, but so far not mathematically proven, that
      every starting number eventuallyterminates at 1.""")

response = input(" Enter a starting number > 0 or QUIT: ")
if not response.isdecimal() or response =='0':
    print('You must enter an interger greater than 0.')
    sys.exit()
n = int(response)
print(n, end='', flush=True)
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(', ' + str(n), end='', flush=True)
print()