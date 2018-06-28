import matplotlib.pyplot as plt
import numpy as np

quantityDemanded = (0, 5000)
demandElasticity = 1

x = np.linspace(2,0, 200)
demand = x * demandElasticity

equilibrium = 1
plt.plot(x, x, label='Demand')
plt.fill_between(x, x, equilibrium, x > 1, label='Consumer Surplus')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('Quantity')
plt.ylabel('Price')

plt.title("Simple Plot")

plt.legend()

plt.show()