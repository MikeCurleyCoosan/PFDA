import numpy as np
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
num_of_entries = 100

np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, num_of_entries)
ages = np.random.randint(21, 65, num_of_entries)

plt.scatter(ages, salaries)

plt.show()