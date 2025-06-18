#Using the Math Module for Calculations
import math

try:
    num = float(input("Enter a number: "))

    if num <= 0:
        print("For natural logarithm and square root, the number must be positive.")
    else:
        
        square_root = math.sqrt(num)
        natural_log = math.log(num)
        sine = math.sin(num) 
        print(f"\nResults for the number {num}:")
        print(f"Square Root: {square_root}")
        print(f"Natural Logarithm (ln): {natural_log}")
        print(f"Sine (in radians): {sine}")

except ValueError:
    print("Invalid input. Please enter a numeric value.")
