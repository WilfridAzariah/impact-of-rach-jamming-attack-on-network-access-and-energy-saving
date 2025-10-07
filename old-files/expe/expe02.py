import numpy as np
import matplotlib.pyplot as plt

# --- Mathematical Model Parameters ---
d_UE_values = [90, 127, 165]  # in cm (used only for labeling)
P_UE_dB = 50
P_attacker_TX_dB = 97.5
gamma = 1.92
alpha = 5

# Attacker distance range in cm
d_attacker_values = np.linspace(1, 450, 449)  # 1cm to 450cm

def calculate_P_attacker_dB(d_attacker):
    return P_attacker_TX_dB - 10 * gamma * np.log10(d_attacker)

def calculate_P_S(P_attacker_dB, P_UE_dB, alpha):
    return 1 / (1 + np.exp(alpha * (P_attacker_dB - P_UE_dB)))

P_attacker_dB_values = calculate_P_attacker_dB(d_attacker_values)
P_S_values = calculate_P_S(P_attacker_dB_values, P_UE_dB, alpha)

# --- Experimental Data ---
#def cm_to_m(x): return [i / 100 for i in x]

# Dataset: UE @ 165.4 cm
attacker_distance_178 = [40, 56.5, 89.4, 126.4, 164.9, 203.9, 243.3, 282.8, 322.4, 362.2, 401.9]
attacker_power_178 = [69, 58.54, 56.23, 55.93, 53.05, 54.1, 56.18, 49.67, 48.75, None, None]
ue_power_178 = [None, None, None, None, None, None, None, None, 49, 47.95, 49.5]
prob_success_178 = [0, 0, 0, 0, 0, 0, 0, 0, 0.6, 1, 1]

# Dataset: UE @ 127.1 cm
attacker_distance_144 = [40, 56.5, 89.4, 126.4, 164.9, 203.9, 243.3, 282.8, 322.4, 362.2, 401.9]
attacker_power_144 = [69.23, 62.25, 58.23, 58.37, 54.85, 55.11, 55.24, 49.11, 44.1, None, None]
ue_power_144 = [None, None, None, None, None, None, None, None, 49.8, 50.12, 48.12]
prob_success_144 = [0, 0, 0, 0, 0, 0, 0, 0, 0.9, 1, 1]

# Dataset: UE @ 90.3 cm
attacker_distance_113 = [40, 56.5, 89.4, 126.4, 164.9, 203.9, 243.3, 282.8, 322.4, 362.2, 401.9]
attacker_power_113 = [69, 63.34, 58.98, 59.22, 53.74, 54.7, 52.13, 49.95, None, None, None]
ue_power_113 = [None, None, None, None, None, None, None, None, 50.28, 50.26, 50.19]
prob_success_113 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]

# --- Plotting ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Left: Probability of success
ax1.plot(d_attacker_values, P_S_values, color='black', label='from Model')
ax1.scatter(attacker_distance_113, prob_success_113, marker='3', s=150, color='blue', label="from Expe (90cm UE)")
ax1.scatter(attacker_distance_144, prob_success_144, marker='4', s=150, color='orange', label="from Expe (127cm UE)")
ax1.scatter(attacker_distance_178, prob_success_178, marker='+', s=150, color='green', label="from Expe (165cm UE)")
ax1.set_title("Probability of UE's Msg3 Success")
#ax1.set_xlabel("$d_{attacker}$ (Attacker Distance to gNB in cm)")
ax1.set_xlabel("$d_{attacker}$ (cm)")
#ax1.set_ylabel("$P_S$ (Msg3 Success Probability)")
ax1.set_ylabel("$P_S$")
ax1.grid(True)
ax1.legend()

# Right: Power at gNB
ax2.plot(d_attacker_values, P_attacker_dB_values, color='black', label='from Model')

# Plot attacker received powers
ax2.scatter(attacker_distance_113, attacker_power_113, marker='3', s=150, color='blue', label='from Expe (90cm UE)')
ax2.scatter(attacker_distance_144, attacker_power_144, marker='4', s=150, color='orange', label='from Expe (127cm UE)')
ax2.scatter(attacker_distance_178, attacker_power_178, marker='+', s=150, color='green', label='from Expe (165cm UE)')

# Plot UE received powers
#ax2.scatter(attacker_distance_113, ue_power_113, marker='3', color='blue', label='UE Power (90cm UE)')
#ax2.scatter(attacker_distance_144, ue_power_144, marker='4', color='orange', label='UE Power (127cm UE)')
#ax2.scatter(attacker_distance_178, ue_power_178, marker='+', color='green', label='UE Power (165cm UE)')

ax2.set_title("Attacker Msg3 Power Received at gNB")
#ax2.set_xlabel("$d_{attacker}$ (Attacker Distance to gNB in cm)")
ax2.set_xlabel("$d_{attacker}$ (cm)")
#ax2.set_ylabel("$p_{RX,attacker}$ (Attacker Msg3 Power in dB)")
ax2.set_ylabel("$p_{RX,attacker}$")
# Set Y-axis limit for the right subplot
ax2.set_ylim(40, 75)
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()
