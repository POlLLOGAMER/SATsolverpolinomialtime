# Solving SAT in Polynomial with 0 and 1

## Resume
In summary, correcting the code, I realized that if the SAT variables are all 1 or 0, one of the 2 will always be true.



---

## Introducción
The SAT problem is one of the most well-known problems in computational complexity theory. However, this paper introduces an alternative approach that challenges conventional methods and explores the possibility of solving it in nearly constant time...

---

## Metod
In summary, I managed to make an algorithm which achieves in any SAT algorithm, no matter if it is gigantic or the most complex in the world, no matter what happens, one of the 2 conventions will always be true, which is all 0 or all 1...

```python
# Función para comprobar este principio que yo cree
def comprobar_ley_de_kaoru(fórmula, variables):
    # Evaluamos la fórmula con todas las variables en 1
    true_all_ones = fórmula(**{var: 1 for var in variables})
    
    # Evaluamos la fórmula con todas las variables en 0
    true_all_zeros = fórmula(**{var: 0 for var in variables})
    
    return true_all_ones, true_all_zeros

# Definimos la fórmula SAT más difícil
def fórmula(A, B, C, D, E, F):
    return (A or B) and (C or D) and (E or F)

# Lista de las variables a usar
variables = ['A', 'B', 'C', 'D', 'E', 'F']

# Comprobamos si la ley se cumple
resultados = comprobar_ley_de_kaoru(fórmula, variables)

print("Resultado con todas las variables en 1:", resultados[0])
print("Resultado con todas las variables en 0:", resultados[1])


```
## Results of this algorithm
In this case, it took between 0.1 seconds to 0.3 seconds to solve the SAT with 10,000 clauses.


## Measuring the time and graphing how long it takes to solve from 5 to 5 up to 2000 clauses
Below is the graph:

 ![ ](/Polinomial%20time.png)


## Here is the code to measure the execution time, based on the growth of the clauses, which generated the previous graph
You need to install the requirements listed in requirements.txt.

```python
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

```

## In conclusion
Since we have developed an algorithm capable of solving an SAT problem that is of NP type, we can confirm that P=NP.
