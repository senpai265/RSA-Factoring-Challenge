import sys

def factorize(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return (i, n // i)
    return None

if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)

input_file = sys.argv[1]

with open(input_file) as f:
    for line in f:
        n = int(line.strip())
        factors = factorize(n)
        if factors is not None:
            print("{}={}*{}".format(n, factors[0], factors[1]))
