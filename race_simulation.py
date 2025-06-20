import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Simulation Parameters
# -----------------------------
race_length = 50                  # Total laps per race
pit_stop_time = 20               # Pit stop under green flag (seconds)
safety_car_pit_time = 10         # Pit stop under safety car (faster)
sc_probability = 0.3             # Probability of safety car in a race
simulations = 1000               # Number of races to simulate
base_lap_time = 90               # Average lap time (seconds)

# Strategy pit laps
strategies = {
    "early": 10,
    "mid": 25,
    "late": 40
}

# Store race results
results = {
    "early": [],
    "mid": [],
    "late": []
}

# -----------------------------
# Run Simulations
# -----------------------------
for _ in range(simulations):
    # Determine if a safety car occurs and when
    has_safety_car = np.random.rand() < sc_probability
    sc_lap = np.random.randint(1, race_length) if has_safety_car else None

    for strat, pit_lap in strategies.items():
        race_time = 0

        # Tire degradation penalty: apply to strategies that pit late
        degradation_penalty = 0.2 if pit_lap > 30 else 0

        # Simulate lap times
        for lap in range(1, race_length + 1):
            if lap == pit_lap:
                continue
            lap_time = np.random.normal(base_lap_time, 0.5)
            if lap < pit_lap:
                lap_time += degradation_penalty  # Add penalty before pit
            race_time += lap_time

        # Add pit stop time
        if has_safety_car and pit_lap == sc_lap:
            race_time += safety_car_pit_time
        else:
            race_time += pit_stop_time

        results[strat].append(race_time)

# -----------------------------
# Print Average Times
# -----------------------------
for strat in strategies:
    avg_time = np.mean(results[strat])
    print(f"{strat.capitalize()} pit strategy average time: {avg_time:.2f} seconds")

# -----------------------------
# Plot Comparison Chart
# -----------------------------
avg_times = [np.mean(results[strat]) for strat in strategies]
labels = [strat.capitalize() for strat in strategies]

plt.figure(figsize=(8, 5))
plt.bar(labels, avg_times, color='gray', edgecolor='black')
plt.title("Average Race Time by Pit Strategy (1000 Simulations)")
plt.ylabel("Total Race Time (seconds)")
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()