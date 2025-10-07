import matplotlib.pyplot as plt
import numpy as np

# Experimental data
power_attacker = np.array([-13.24249914, -9.134185682, -3.027857035, 1.382638703, 6.900479473])
prob_success_exp = np.array([1, 1, 0.6, 0, 0])
noise_exp = np.array([-11.80478547, -10.06853648, -4.962127285, np.nan, np.nan])
ue_power = np.array([-7.228554178, -7.228554178, -7.228554178, -7.228554178, -7.228554178])
threshold = -3.39134522

# Calculate UE power - threshold for a constant level
ue_minus_threshold = np.mean(ue_power - threshold)

# --- Right Plot (Noise Model) ---
noise_model = power_attacker  # Model: noise = attacker power

# --- Left Plot (Prob Model) ---
# Calculate model probability
prob_model = []
for i in range(len(power_attacker)):
    if i < len(ue_power) and not np.isnan(ue_power[i]):
        total_noise = noise_model[i] + threshold
        prob = 1 if ue_power[i] > total_noise else 0
    else:
        prob = np.nan
    prob_model.append(prob)

# Convert to numpy array for plotting
prob_model = np.array(prob_model)

# --- Plotting ---
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Left Plot: UE Success Probability
axs[0].plot(power_attacker, prob_success_exp, 'x', label='Experiment')
axs[0].plot(power_attacker, prob_model, 'k-', label='Model')
axs[0].set_title('Prob of UE Success vs Power of Attacker')
axs[0].set_xlabel('$p_{attacker}$ (dB)')
axs[0].set_ylabel('$P_{S,0}$')
axs[0].set_ylim(-0.1, 1.1)
axs[0].grid(True)
axs[0].legend()

# Right Plot: Noise Power
axs[1].plot(power_attacker, noise_exp, 'x', label='Experiment')
axs[1].plot(power_attacker, noise_model, 'k-', label='Model')
axs[1].set_title('Noise Power vs Power of Attacker')
axs[1].set_xlabel('$p_{attacker}$ (dB)')
axs[1].set_ylabel('$p_{th,0}$ (dB)')
# Add horizontal red dashed line for "UE Power - Threshold"
axs[1].axhline(y=ue_minus_threshold, color='r', linestyle='--', label='$p_{UE} - \delta$')
axs[1].grid(True)
axs[1].legend()

plt.tight_layout()
plt.show()
