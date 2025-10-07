import matplotlib.pyplot as plt
import numpy as np

# Parameters
P_noise = 21.1
P_attacker = 51
alpha = 0.12
delta = 12
P_active = 68.75
P_sleep = 29.92
T_active = 8
T_sleep = 10
T_transition_up = 5
T_transition_down = 1
T_cycle = T_active + T_sleep + T_transition_up + T_transition_down
Ta_values = [0.1, 1, 2]

# Real data (in mW)
real_data_mW_dict = {
    0.1: [
        68464, 68684, 68464, 68530, 69146, 68948, 68970, 68992,
    68684, 33374, 29656, 29546, 29458, 29370, 29326, 29788,
    29766, 29678, 29656, 29854, 34342, 29436, 47498, 31372
    ],
    1: [
    71610, 68090, 68046, 68772, 68750, 68948, 68926, 68882,
    69454, 39292, 30668, 29876, 29810, 29744, 29898, 29876,
    29766, 30206, 29744, 30844, 34188, 31658, 70114, 31284
    ],
    2: [72952, 70312, 71104, 70158, 70048, 70180, 70686, 70488, 69982,
    69916, 69894, 70004, 69982, 70114, 70070, 70224, 70202, 70224,
    70576, 70070, 70444, 70422, 70378, 70598]
}

# Convert to Watts and create time arrays
real_data_W_dict = {k: [v / 1000 for v in vs] for k, vs in real_data_mW_dict.items()}
real_time_points = np.arange(0, T_cycle, 1)


# Slope transitions
def transition_power(start_power, end_power, duration, time_in_state):
    return start_power + (end_power - start_power) * (time_in_state / duration)

def avg_measured_power(Ta):
    return (1 / Ta) * P_attacker + ((Ta - 1) / Ta) * P_noise

def can_gnb_sleep(Ta):
    P_th_infty = avg_measured_power(Ta)
    return P_attacker < (P_th_infty + delta)

def total_energy(Ta):
    if can_gnb_sleep(Ta):
        E_active = P_active * T_active
        E_sleep = P_sleep * T_sleep
        E_trans_down = ((P_active + P_sleep) / 2) * T_transition_down
        E_trans_up = ((P_sleep + P_active) / 2) * T_transition_up
        return E_active + E_trans_down + E_sleep + E_trans_up
    else:
        return P_active * T_cycle

total_energies = [total_energy(Ta) for Ta in Ta_values]
real_total_energies = {
    Ta: sum(real_data_W_dict[Ta]) for Ta in real_data_W_dict
}

# Power profiles
time_points = np.arange(0, T_cycle, 0.1)
power_profiles = []

for Ta in Ta_values:
    profile = []
    if can_gnb_sleep(Ta):
        for t in time_points:
            if t < T_active:
                profile.append(P_active)
            elif t < T_active + T_transition_down:
                t_in_transition = t - T_active
                p = transition_power(P_active, P_sleep, T_transition_down, t_in_transition)
                profile.append(p)
            elif t < T_active + T_transition_down + T_sleep:
                profile.append(P_sleep)
            elif t < T_cycle:
                t_in_transition = t - (T_active + T_transition_down + T_sleep)
                p = transition_power(P_sleep, P_active, T_transition_up, t_in_transition)
                profile.append(p)
    else:
        profile = [P_active] * len(time_points)
    power_profiles.append(profile)

# Define colors matching the modeled lines/bar chart
color_map = {
    0.1: '#1f77b4',  # Blue
    1: '#ff7f0e',  # Orange
    2: '#2ca02c'  # Green
}

# Plotting
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Bar chart (without real data as bar)
bar_labels = ['Normal', 'Attacked\nTa=1', 'Attacked\nTa=2']
bars = axes[0].bar(bar_labels, total_energies, color="white", edgecolor=['#1f77b4', '#ff7f0e', '#2ca02c'], linewidth=2)

# Apply different border styles
linestyles = ['dashed', 'dotted', 'dashdot']
for i, bar in enumerate(bars):
    bar.set_linestyle(linestyles[i])

# Plot modeled energy line
for i, Ta in enumerate(Ta_values):
    if Ta in real_total_energies:
        color = color_map.get(Ta, 'black')
        if (Ta == 0.1) :
            axes[0].scatter(i, total_energies[i], color=color, marker='_', s=1, label=f'Normal from Model')
        if (Ta == 1) :
            axes[0].scatter(i, total_energies[i], color=color, marker='_', s=1, label=f'Attacked from Model (Ta={Ta})')
        if (Ta == 2) :
            axes[0].scatter(i, total_energies[i], color=color, marker='_', s=1, label=f'Attacked from Model (Ta={Ta})')


# Plot real energy dots
for i, Ta in enumerate(Ta_values):
    if Ta in real_total_energies:
        color = color_map.get(Ta, 'black')
        if (Ta == 0.1) :
            axes[0].scatter(i, real_total_energies[Ta], color=color, marker='3', s=100, label=f'Normal from Expe')
        if (Ta == 1) :
            axes[0].scatter(i, real_total_energies[Ta], color=color, marker='4', s=100, label=f'Attacked from Expe (Ta={Ta})')
        if (Ta == 2) :
            axes[0].scatter(i, real_total_energies[Ta], color=color, marker='+', s=100, label=f'Attacked from Expe (Ta={Ta})')

axes[0].set_title("gNB's Total Energy Consumption per Cycle")
axes[0].set_ylabel('Energy (J)')
axes[0].set_ylim([0, max(total_energies + list(real_total_energies.values())) * 1.2])
axes[0].legend()

# Line chart
for idx, Ta in enumerate(Ta_values):
    if (Ta == 0.1) :
        axes[1].plot(time_points, power_profiles[idx], linestyle='dashed', label=f'Normal from Model', linewidth=2)
    if (Ta == 1) :
        axes[1].plot(time_points, power_profiles[idx], linestyle='dotted', label=f'Attacked from Model (Ta={Ta})', linewidth=2)
    if (Ta == 2) :
        axes[1].plot(time_points, power_profiles[idx], linestyle='dashdot', label=f'Attacked from Model (Ta={Ta})', linewidth=2)
	

# Plot real data with matching colors
for Ta, data_W in real_data_W_dict.items():
    color = color_map.get(Ta, 'black')
    if (Ta == 0.1) :
        axes[1].scatter(real_time_points, data_W, label=f'Normal from Expe', marker='3', s=100, color=color)
    if (Ta == 1) :
        axes[1].scatter(real_time_points, data_W, label=f'Attacked from Model (Ta={Ta})', marker='4', s=100, color=color)
    if (Ta == 2) :
        axes[1].scatter(real_time_points, data_W, label=f'Attacked from Model (Ta={Ta})', marker='+', s=100, color=color)
	
axes[1].set_title("gNB's Power Consumption Profile in a Cycle")
axes[1].set_xlabel('Time (s)')
axes[1].set_ylabel('Power (W)')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.show()
