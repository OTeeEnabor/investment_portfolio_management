import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
import numpy as np

# create a model
model = pyo.ConcreteModel()

# define the optimisation problem variables
model.x = pyo.Var(bounds=(-np.inf, 3))
model.y = pyo.Var(bounds=(0, np.inf))

# assign the model variable
x = model.x
y = model.y

# create constraints
model.C1 = pyo.Constraint(expr=x + y <= 8)
model.C2 = pyo.Constraint(expr=8 * x + 3 * y >= -24)
model.C3 = pyo.Constraint(expr=-6 * x + 8 * y <= 48)
model.C4 = pyo.Constraint(expr=3 * x + 5 * y <= 15)
# model.C5 = pyo.Constraint(expr=x <= 3)
# model.C6 = pyo.Constraint(expr=y >= 0)


# define objective expression
obj_expr = -4 * x + 2 * y
model.obj = pyo.Objective(expr=obj_expr, sense=minimize)

opt = SolverFactory("glpk")
opt.solve(model)

model.pprint()

x_value = pyo.value(x)
y_value = pyo.value(y)

print("x=", x_value)
print("y=", y_value)
