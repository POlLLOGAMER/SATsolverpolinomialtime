import time
import math
import matplotlib.pyplot as plt

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
    start_time = time.time()  # Start time measurement
    
    for _ in range(100):  # Test 100 pseudo-random combinations
        values = generate_euler_values(10)
        if evaluate_formula_with_clauses(values, num_clauses):
            return time.time() - start_time  # Return execution time
    
    return time.time() - start_time  # If no solution is found, return the time

# Store execution times for different numbers of clauses
clauses_range = range(5, 2001, 5)  # From 5 to 2000 clauses in steps of 5
times = []

# Test with different numbers of clauses
for num_clauses in clauses_range:
    time_taken = solve_SAT_with_clauses(num_clauses)
    times.append(time_taken)

# Create the plot
plt.plot(clauses_range, times, marker='o')
plt.title("Execution time as a function of the number of clauses")
plt.xlabel("Number of clauses")
plt.ylabel("Execution time (seconds)")
plt.grid(True)
plt.show()
