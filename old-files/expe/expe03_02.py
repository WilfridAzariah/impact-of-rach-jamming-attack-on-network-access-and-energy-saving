import numpy as np
import matplotlib.pyplot as plt

# Simulation Parameters
trans_down = 1
trans_up = 6
stay_active = 17
total_cycle = trans_down*2 + trans_up*2 + stay_active
p_idle = 28
p_sleep = 51
p_active = 72

# Time resolution
dt = 1

# First profile: constant 50.8W for total_cycle seconds
t1 = np.arange(0, total_cycle, dt)
p1 = np.full_like(t1, p_sleep)

# Second profile
# Segment 1: transition down 1s from 50.8 to 30
t2_1 = np.arange(0, trans_down, dt)
p2_1 = np.linspace(p_sleep, p_idle, len(t2_1))

# Segment 2: transition up 6s from 30 to 72
t2_2 = np.arange(0, trans_up, dt)
p2_2 = np.linspace(p_idle, p_active, len(t2_2))

# Segment 3: constant 72W for 17s
t2_3 = np.arange(0, stay_active, dt)
p2_3 = np.full_like(t2_3, p_active)

# Segment 4: transition down 1s from 72 to 30
t2_4 = np.arange(0, trans_down, dt)
p2_4 = np.linspace(p_active, p_idle, len(t2_4))

# Segment 5: transition up 6s from 30 to 50.8
t2_5 = np.arange(0, trans_up, dt)
p2_5 = np.linspace(p_idle, p_sleep, len(t2_5))

# Combine second profile
p2 = np.concatenate([p2_1, p2_2, p2_3, p2_4, p2_5])
t2 = np.arange(0, len(p2)*dt, dt)

# Mock experiment data with slight randomness, typed directly
data1 = [
    51, 48.1, 48.2, 48.2, 54.1, 48.2, 48.2, 54.2, 51, 53.5,  
    48.2, 48.2, 54.2, 48.1, 51.1, 48.2, 54.1, 48.2, 53.5, 51,  
    48.2, 48.1, 51, 48.2, 54.2, 54.2, 48.2, 48.2, 51.1, 53.5,  
    54.2
]
# Repeat to match length
#data1 = np.array(data1 * int(len(t1)/len(data1)))

data2 = [
    57.6,
    30.7, 31.5, 28.4, 39.5, 39.5, 48.3, 74.8,
	71.8, 71.6, 71.6, 71.6, 72.6, 72.1, 72, 71.9, 71.8, 72.6, 71.9, 75, 72.7, 74.4, 72.3, 72.3, 71.3,
	47.8,
	30.7, 30.3, 33.7, 28.6, 39.5
]
#data2 = np.array(data2 * int(len(t2)/len(data2)))

# Energy calculation
energy1 = np.trapz(p1, t1)
energy2 = np.trapz(p2, t2)
energy1_exp = np.trapz(data1, t1[:len(data1)])
energy2_exp = np.trapz(data2, t2[:len(data2)])

# Plot
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Left plot: simulation lines and experiment dots
axs[0].plot(t1, p1, label="Normal (Model)", color='blue', linestyle='dashed')
axs[0].plot(t2, p2, label="Attacked (Model)", color='red', linestyle='dotted')
axs[0].scatter(t1[:len(data1)], data1, label="Normal (Expe)", color='blue', marker='3', s=100)
axs[0].scatter(t2[:len(data2)], data2, label="Attacked (Expe)", color='red', marker='4', s=100)
axs[0].set_xlabel("Time (s)")
axs[0].set_ylabel("Power (W)")
axs[0].legend()
axs[0].grid(True)
axs[0].set_ylim(0, 80)
axs[0].set_title("gNB Power Consumption Profile in a Cycle")

# Right plot: bar chart of energies
#axs[1].bar(["Profile 1 Sim", "Profile 2 Sim", "Profile 1 Exp", "Profile 2 Exp"],
#           [energy1, energy2, energy1_exp, energy2_exp])
bars = axs[1].bar(["Normal", "Attacked"],
           [energy1, energy2], color='#D3D3D3', edgecolor=['blue', 'red'], linewidth=2)
# Apply different border styles
linestyles = ['dashed', 'dotted']
for i, bar in enumerate(bars):
    bar.set_linestyle(linestyles[i])
# Plot modeled energy line
axs[1].scatter(0, energy1, color='blue', marker='_', s=1, label=f'Normal (Model)')
axs[1].scatter(1, energy2, color='red', marker='_', s=1, label=f'Attacked (Model)')
# Plot real energy dots
axs[1].scatter(0, energy1_exp, color='blue', marker='3', s=100, label=f'Normal (Expe)')
axs[1].scatter(1, energy2_exp, color='red', marker='4', s=100, label=f'Attacked (Expe)')
axs[1].set_ylabel("Energy (Joules)")
axs[1].set_title("gNB Total Energy in a Cycle per Profile")
axs[1].grid(True, axis='y')
axs[1].legend()

plt.tight_layout()
plt.show()
