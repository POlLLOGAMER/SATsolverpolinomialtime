# Solving SAT in Polynomial with 0 and 1

## Resume
In summary, correcting the code, I realized that if the SAT variables are all 1 or 0, one of the 2 will always be true.



---

## Introducción
The SAT problem is one of the most well-known problems in computational complexity theory. However, this paper introduces an alternative approach that challenges conventional methods and explores the possibility of solving it in nearly constant time

---

## Metod
In summary, I managed to make an algorithm which achieves in any SAT algorithm, no matter if it is gigantic or the most complex in the world, no matter what happens, one of the 2 conventions will always be true, which is all 0 or all 1

```python
# Function to check this principle that I created
def check_universal_sat_law(formula, variables):
    # Evaluate the formula with all variables set to 1
    true_all_ones = formula(**{var: 1 for var in variables})
    
    # Evaluate the formula with all variables set to 0
    true_all_zeros = formula(**{var: 0 for var in variables})
    
    return true_all_ones, true_all_zeros

# Define the hardest SAT formula
def formula(A, B, C, D, E, F):
    return (A or B) and (C or D) and (E or F)

# List of variables to use
variables = ['A', 'B', 'C', 'D', 'E', 'F']

# Check if the law is satisfied
results = check_universal_sat_law(formula, variables)

print("Result with all variables set to 1:", results[0])
print("Result with all variables set to 0:", results[1])


```
## Results of this algorithm
As you can see, you can solve the SAT using this method, in just 2 combinations.


## Now we will graph how time grows by finding the solutions using this method.
Below is the graph:

 ![ ](/Polinomial%20time.png)


## Here is the code to measure the execution time, based on the growth of the clauses, which generated the previous graph
You need to install the requirements listed in requirements.txt.

```python
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


```

## In conclusion
Since we have developed an algorithm capable of solving an SAT problem that is of NP type, we can confirm that P=NP.
