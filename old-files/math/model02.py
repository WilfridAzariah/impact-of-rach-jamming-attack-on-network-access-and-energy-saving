import numpy as np
import matplotlib.pyplot as plt

# Define the given parameters
P_UE_values = [820, 860, 900]  # Different values of P_UE to compare
P_attacker_values = np.linspace(700, 1020, 200)  # Range of P_attacker from 700 to 1020 (200 points)

# Define the sigmoid function P_S based on the equation
def calculate_P_S(P_attacker, P_UE):
    return 1 / (1 + np.exp(P_attacker - P_UE))

# Plotting the results for different P_UE values
plt.figure(figsize=(8, 6))

# Loop through each P_UE value and plot the corresponding P_S
for P_UE in P_UE_values:
    P_S_values = calculate_P_S(P_attacker_values, P_UE)
    plt.plot(P_attacker_values, P_S_values, label=f"$P_{{UE}} = {P_UE}$ dB")

# Display the plot with labels and title
plt.xlabel(r"$P_{attacker}$ (dB)")
plt.ylabel(r"$P_S$")
plt.title("Sigmoid Output $P_S$ vs Attacker's Power $P_{attacker}$ for Different $P_{UE}$ Values")
plt.grid(True)
plt.legend()
plt.show()
