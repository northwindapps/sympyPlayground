from sympy import symbols, simplify
# x = Symbol('x')
# print(limit(sin(x)/x, x, 0))

# Define symbols
x = symbols('x')

# Create an expression
expr = (x**2 + 2*x + 1)/(x + 1)

# Simplify the expression
simplified_expr = simplify(expr)

# Print the simplified expression
print(simplified_expr)

# https://stackoverflow.com/questions/43700354/conda-and-visual-studio-code-debugging