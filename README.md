# Monte Carlo Simulation of F1 Pit Stop Strategy

This project simulates different pit stop strategies in a 50-lap race using Monte Carlo methods. It models the impact of random safety car deployment, tire degradation, and pit stop timing to analyze which strategy (early, mid, or late) tends to result in the shortest total race time.

## Simulation Details

- 1000 simulated races
- One mandatory pit stop per strategy
- Random chance of a safety car each race
- Pitting under safety car gives a time advantage
- Lap time includes random variation and degradation penalty for late pit stops

## Strategies Compared

- **Early:** Pit on lap 10
- **Mid:** Pit on lap 25
- **Late:** Pit on lap 40

## Tools Used

- Python
- NumPy
- Matplotlib
- Visual Studio Code

## Output

- Printed average race time for each strategy
- Bar chart comparing the three strategies visually

## Takeaways

This project demonstrates how simulation can be used to evaluate decision-making under uncertainty in racing environments. It can be extended to model tire compound changes, multi-driver strategies, or real-world telemetry in the future.