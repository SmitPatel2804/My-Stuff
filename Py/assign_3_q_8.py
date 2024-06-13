from scipy.stats import binom

def f(x):
    return 1 / x

# Define the binomial random variable with parameters p = 1/4 and n = 20
p = 1/4
n = 20
rv = binom(n, p)

# Calculate the expected value of f(X)
expected_f_X = sum([f(x) * rv.pmf(x) for x in range(1, n+1)])


# Calculate f of the expected value of X
f_expected_X = f(rv.mean())

# Verify Jensen's Inequality: E[f(X)] >= f(E[X])
if expected_f_X >= f_expected_X:
    print("Jensen's Inequality is satisfied.")
else:
    print("Jensen's Inequality is not satisfied.")

# Print the defined function, the defined PMF, and the output
print("Defined function: f(x) = 1/x, x > 0")
print("Defined PMF: Binomial distribution with parameters p = 1/4 and n = 20")
print("Expected value of f(X):", expected_f_X)
print("f(Expected value of X):", f_expected_X)
