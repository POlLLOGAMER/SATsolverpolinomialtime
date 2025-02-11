import time
import math

# Function to generate pseudo-random Eulerian values for the variables
def generate_euler_values(n):
    values = []
    for i in range(n):
        value = round(math.sin(math.e * i) % 1, 2)
        values.append(1 if value > 0.5 else 0)
    return values

# Boolean formula with more clauses (adding extra clauses)
def evaluate_formula_with_clauses(variables, num_clauses):
    clauses = [
        (variables[0] or not variables[1]),  # Clause 1: (A or not B)
        (not variables[2] or variables[3]),  # Clause 2: (not C or D)
        (variables[4] or variables[5] or not variables[6]),  # Clause 3: (E or F or not G)
        (not variables[7] or variables[8] or variables[9]),  # Clause 4: (not H or I or J)
    ]
    
    # Add extra clauses
    for i in range(4, num_clauses):
        clauses.append(variables[i % 10] or not variables[(i + 1) % 10])
    
    return all(clauses)

# Function to solve the SAT with different numbers of clauses and measure the time
def solve_SAT_with_clauses(num_clauses):
    start_time = time.time()  # Measure the start time
    
    for _ in range(100):  # Try 100 pseudo-random combinations
        values = generate_euler_values(10)
        if evaluate_formula_with_clauses(values, num_clauses):
            return time.time() - start_time  # Return the execution time
    
    return time.time() - start_time  # If no solution is found, return the time

# Run with 10,000 clauses and measure the time
num_clauses = 10000
time_taken = solve_SAT_with_clauses(num_clauses)
print(f"Execution time for {num_clauses} clauses: {time_taken} seconds")
