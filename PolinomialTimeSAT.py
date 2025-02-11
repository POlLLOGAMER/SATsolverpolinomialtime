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
