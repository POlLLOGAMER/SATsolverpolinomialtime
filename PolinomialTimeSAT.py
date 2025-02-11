import matplotlib.pyplot as plt
import numpy as np
import time  # To measure execution time

# Function to check the SAT Law with a more complex SAT problem
def check_sat_law(formula, variables):
    # Evaluate the formula with all variables set to 1
    true_all_ones = formula(*[1 for _ in variables])
    
    # Evaluate the formula with all variables set to 0
    true_all_zeros = formula(*[0 for _ in variables])
    
    return true_all_ones, true_all_zeros

# Define the hardest SAT formula
def formula(*args):
    # The number of variables is flexible here
    return any(args)  # Simple OR clause example

# List of variables to use, now expanded up to number 100
variables = [f'V{i}' for i in range(1, 101)]

# Store the results
execution_times = []  # To store execution times
num_clauses = []  # To store the number of clauses

# Test every 5 clauses
for i in range(5, 1001, 5):  # Test from 1 to 100 clauses, in steps of 5
    current_vars = variables[:i]
    
    # Measure execution time
    start_time = time.time()
    check_sat_law(formula, current_vars)
    end_time = time.time()
    
    # Store execution time and the number of clauses
    execution_times.append(end_time - start_time)
    num_clauses.append(i)

# Data for the plot
time_data = np.array(num_clauses)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(time_data, execution_times, marker='o', color='r', label='Execution Time')
plt.xlabel('Number of Clauses')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs Number of Clauses')
plt.grid(True)
plt.legend()
plt.show()
