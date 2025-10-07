import numpy as np
import matplotlib.pyplot as plt

# --- Mathematical Model Parameters ---
d_UE = 127  # in cm (used only for labeling)
P_UE_dB_values = [49.3, 51.4, 60.4]
P_attacker_TX_dB_values = [101.46, 100.91, 95.76]
gamma_values = [2.11, 2.09, 1.75]
alpha = 5

# Attacker distance range in cm
d_attacker_values = np.linspace(1, 450, 449)  # 1cm to 450cm

def calculate_P_attacker_dB(d_attacker, P_attacker_TX_dB, gamma):
    return P_attacker_TX_dB - 10 * gamma * np.log10(d_attacker)

def calculate_P_S(P_attacker_dB, P_UE_dB, alpha):
    return 1 / (1 + np.exp(alpha * (P_attacker_dB - P_UE_dB)))

P_attacker_dB_49 = calculate_P_attacker_dB(d_attacker_values, P_attacker_TX_dB_values[0], gamma_values[0])
P_attacker_dB_51 = calculate_P_attacker_dB(d_attacker_values,  P_attacker_TX_dB_values[1], gamma_values[1])
P_attacker_dB_60 = calculate_P_attacker_dB(d_attacker_values,  P_attacker_TX_dB_values[2], gamma_values[2])
P_S_values_49 = calculate_P_S(P_attacker_dB_49, P_UE_dB_values[0], alpha)
P_S_values_51 = calculate_P_S(P_attacker_dB_51, P_UE_dB_values[1], alpha)
P_S_values_60 = calculate_P_S(P_attacker_dB_60, P_UE_dB_values[2], alpha)

# --- Experimental Data ---
#def cm_to_m(x): return [i / 100 for i in x]

# Dataset: UE @ 60 dB
attacker_distance_60 = [40, 56.5, 89.4, 126.4, 164.9, 203.9, 243.3, 282.8, 322.4, 362.2, 401.9]
attacker_power_60 = [69.9, 61.9, 61.8, 59.8, None, None, None, None, None, None, None]
ue_power_60 = [None, None, None, 61.1, 58.2, 61, 61.5, 60.6, 60, 59.9, 60.7]
prob_success_60 = [0, 0, 0, 0.8, 1, 1, 1, 1, 1, 1, 1]

# Dataset: UE @ 51.4 dB
attacker_distance_51 = [40, 56.5, 89.4, 126.4, 164.9, 203.9, 243.3, 282.8, 322.4, 362.2, 401.9]
attacker_power_51 = [69.5, 61.4, 59.3, 58.4, 57.6, 50.3, None, None, None, None, None]
ue_power_51 = [None, None, None, None, None, 51.8, 51, 51.1, 52, 50.9, 51.8]
prob_success_51 = [0, 0, 0, 0, 0, 0.8, 1, 1, 1, 1, 1]

# Dataset: UE @ 49.3 dB
attacker_distance_49 = [40, 56.5, 89.4, 126.4, 164.9, 203.9, 243.3, 282.8, 322.4, 362.2, 401.9]
attacker_power_49 = [69.2, 62.2, 58.2, 58.3, 54.8, 55.1, 55.2, 49.1, 44.1, None, None]
ue_power_49 = [None, None, None, None, None, None, None, None, 49.8, 50.1, 48.1]
prob_success_49 = [0, 0, 0, 0, 0, 0, 0, 0, 0.9, 1, 1]

# --- Plotting ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Left: Probability of success
ax1.plot(d_attacker_values, P_S_values_60, color='blue', linestyle='dotted', label='from Model for 60dB UE')
ax1.plot(d_attacker_values, P_S_values_51, color='orange', linestyle='dashed', label='from Model for 51dB UE')
ax1.plot(d_attacker_values, P_S_values_49, color='green', linestyle='dashdot', label='from Model for 49dB UE')
ax1.scatter(attacker_distance_60, prob_success_60, marker='3', s=150, color='blue', label="from Expe for 60dB UE")
ax1.scatter(attacker_distance_51, prob_success_51, marker='4', s=150, color='orange', label="from Expe for 51dB UE")
ax1.scatter(attacker_distance_49, prob_success_49, marker='+', s=150, color='green', label="from Expe for 49dB UE")
ax1.set_title("Probability of UE's Msg3 Success")
#ax1.set_xlabel("$d_{attacker}$ (Attacker Distance to gNB in cm)")
ax1.set_xlabel("$d_{attacker}$ (cm)")
#ax1.set_ylabel("$P_S$ (Msg3 Success Probability)")
ax1.set_ylabel("$P_S$")
ax1.grid(True)
ax1.legend()

# Right: Power at gNB
ax2.plot(d_attacker_values, P_attacker_dB_60, color='blue', linestyle='dotted', label='from Model (60dB UE)')
ax2.plot(d_attacker_values, P_attacker_dB_51, color='orange', linestyle='dashed', label='from Model (51dB UE)')
ax2.plot(d_attacker_values, P_attacker_dB_49, color='green', linestyle='dashdot', label='from Model (49dB UE)')

# Plot attacker received powers
ax2.scatter(attacker_distance_60, attacker_power_60, marker='3', s=150, color='blue', label='from Expe (60dB UE)')
ax2.scatter(attacker_distance_51, attacker_power_51, marker='4', s=150, color='orange', label='from Expe (51dB UE)')
ax2.scatter(attacker_distance_49, attacker_power_49, marker='+', s=150, color='green', label='from Expe (49dB UE)')

# Plot UE received powers
#ax2.scatter(attacker_distance_60, ue_power_60, marker='x', color='blue', label='UE Power (60dB UE)')
#ax2.scatter(attacker_distance_51, ue_power_51, marker='x', color='orange', label='UE Power (51dB UE)')
#ax2.scatter(attacker_distance_49, ue_power_49, marker='x', color='green', label='UE Power (49dB UE)')

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
