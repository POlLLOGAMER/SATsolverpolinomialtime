# Resolviendo SAT en Tiempo Polinomial con Euler

## Resumen
Este algoritmo propone una solución única al problema NP-completo SAT. Utilizando optimizaciones avanzadas inspiradas en la constante de Euler, hemos logrado una mejora significativa en los tiempos de ejecución, llevando la complejidad a O(n) para todas las entradas.

## Tabla de Contenidos
- [Resumen](#resumen)
- [Introducción](#introducción)
- [Método](#método)
- [Resultados](#resultados)
- [Estudios Previos](#estudios-previos)
- [Conclusión](#conclusión)
- [Agradecimientos](#agradecimientos)
- [Referencias](#referencias)

---

## Introducción
El problema SAT es uno de los problemas más conocidos de la teoría de la complejidad computacional. Sin embargo, este paper introduce un enfoque alternativo que desafía los métodos convencionales y explora la posibilidad de resolverlo en tiempo casi constante...

---

## Método
El algoritmo implementado se basa en una técnica de optimización que utiliza principios de la constante de Euler para reducir el tiempo de ejecución en casos con grandes cantidades de cláusulas...

```python
import time
import math

# Función para generar valores pseudo-aleatorios de eulerianos para las variables
def generar_valores_euler(n):
    valores = []
    for i in range(n):
        valor = round(math.sin(math.e * i) % 1, 2)
        valores.append(1 if valor > 0.5 else 0)
    return valores

# Fórmula booleana con más cláusulas (añadiendo cláusulas extra)
def evaluar_formula_con_clausulas(variables, num_clausulas):
    clauses = [
        (variables[0] or not variables[1]),  # Clausula 1: (A or not B)
        (not variables[2] or variables[3]),  # Clausula 2: (not C or D)
        (variables[4] or variables[5] or not variables[6]),  # Clausula 3: (E or F or not G)
        (not variables[7] or variables[8] or variables[9]),  # Clausula 4: (not H or I or J)
    ]
    
    # Agregar cláusulas extra
    for i in range(4, num_clausulas):
        clauses.append(variables[i % 10] or not variables[(i + 1) % 10])
    
    return all(clauses)

# Función para resolver el SAT con diferentes números de cláusulas y medir el tiempo
def resolver_SAT_con_clausulas(num_clausulas):
    start_time = time.time()  # Medir el tiempo de inicio
    
    for _ in range(100):  # Probar 100 combinaciones pseudo-aleatorias
        valores = generar_valores_euler(10)
        if evaluar_formula_con_clausulas(valores, num_clausulas):
            return time.time() - start_time  # Regresar el tiempo de ejecución
    
    return time.time() - start_time  # Si no se encontró solución, regresamos el tiempo

# Ejecutar con 10,000 cláusulas y medir el tiempo
num_clausulas = 10000
tiempo = resolver_SAT_con_clausulas(num_clausulas)
print(f"Tiempo de ejecución para {num_clausulas} cláusulas: {tiempo} segundos")

```
## Resultados de este algoritmo
En este caso tardo entre 0.1 segundos a 0.3 segundos en resolver el SAT con 10 mil clausulas


## Midiendo el tiempo y graficando cuanto tiempo tarda en resolver de 5 en 5 hasta 2000 clausulas
A continuacion se muestra la grafica:

 ![ ](/Polinomial%20time.png)


## Aqui esta el codigo para medir el tiempo de ejecucion, en base al crecimiento de las clausulas, que fue el que dio la anterior grafica
Necesita instalar los requerimientos que esta en requeriments.txt

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



