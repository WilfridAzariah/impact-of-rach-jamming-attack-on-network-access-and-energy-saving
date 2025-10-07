import numpy as np
import matplotlib.pyplot as plt

# Parameters
d_UE_values = [90, 127, 165]  # in meters (not used in this simplified model)
P_UE_dB = 50  # Msg3 power in dB received at gNB
P_attacker_TX_dB = 97.5  # Attacker's TX power in dB
gamma = 1.92  # Path loss exponent

# Distance range for attacker [1, 450] meters (log range)
d_attacker_values = np.linspace(1, 450, 449)

# Compute received power from attacker in dB
def calculate_P_attacker_dB(d_attacker):
    return P_attacker_TX_dB - 10 * gamma * np.log10(d_attacker)

# Sigmoid function in dB domain
def calculate_P_S(P_attacker_dB, P_UE_dB, alpha=0.5):
    return 1 / (1 + np.exp(alpha * (P_attacker_dB - P_UE_dB)))

# Compute attacker power and P_S
P_attacker_dB_values = calculate_P_attacker_dB(d_attacker_values)
P_S_values = calculate_P_S(P_attacker_dB_values, P_UE_dB)

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Left plot: P_S vs. d_attacker
axs[0].plot(d_attacker_values, P_S_values, color='blue', label=f"$P_{{UE}} = {P_UE_dB}$ dB")
axs[0].set_xlabel(r"$d_{attacker}$ (meters)")
axs[0].set_ylabel(r"$P_S$")
axs[0].set_title(r"$P_S$ vs. Attacker Distance $d_{attacker}$")
axs[0].grid(True)
axs[0].legend()

# Right plot: P_attacker vs. d_attacker
axs[1].plot(d_attacker_values, P_attacker_dB_values, color='black', label=r"$P_{attacker}^{Rx}$")
axs[1].axhline(P_UE_dB, color='red', linestyle='--', linewidth=1, label=f"$P_{{UE}} = {P_UE_dB}$ dB")
axs[1].set_xlabel(r"$d_{attacker}$ (meters)")
axs[1].set_ylabel(r"$P_{attacker}^{Rx}$ (dB)")
axs[1].set_title(r"Attacker Received Power vs. Distance")
axs[1].grid(True)
axs[1].legend()

plt.tight_layout()
plt.show()
