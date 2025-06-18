# Calculate Factorial Using a Function
# Function to calculate factorial using recursion
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Sample number
n=int(input("Enter a number to calculate its factorial: "))

# Call the function and print the result
result = factorial(n)
print(f"The factorial of {n} is: {result}")

