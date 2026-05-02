from pulp import LpMaximize, LpProblem, LpVariable

# Create problem
model = LpProblem(name="profit-maximization", sense=LpMaximize)

# Decision variables
x = LpVariable(name="Product_A", lowBound=0)
y = LpVariable(name="Product_B", lowBound=0)

# Objective function (maximize profit)
model += 20 * x + 30 * y, "Profit"

# Constraints
model += 2 * x + y <= 100  # Resource 1
model += x + 2 * y <= 80   # Resource 2

# Solve
model.solve()

# Output results
print("Status:", model.status)
print("Product A units:", x.value())
print("Product B units:", y.value())
print("Maximum Profit:", model.objective.value())