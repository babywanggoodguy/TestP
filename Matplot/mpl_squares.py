import matplotlib.pyplot as plt

input_values = list(range(1, 5001))
semi = [input_value**3 for input_value in input_values]
plt.plot(input_values, semi, linewidth=5)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)

plt.show()