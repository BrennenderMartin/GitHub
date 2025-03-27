import matplotlib
matplotlib.use('Agg')  # Use an interactive backend
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('result.csv')

# Print the CSV preview
print("CSV preview:")
print(df.head())

# Create a figure with 3 subplots sharing the x-axis (time)
fig, axs = plt.subplots(3, 1, figsize=(8, 10), sharex=True)
fig.suptitle('Results vs Time :)')

# Plot Acceleration vs Time
axs[0].plot(df['Time(t)'], df['Acceleration(a)'], marker='o', linestyle='-', color='red')
axs[0].set_ylabel('Acceleration (a)')
axs[0].grid(True)

# Plot Velocity vs Time
axs[1].plot(df['Time(t)'], df['Velocity(v)'], marker='o', linestyle='-', color='blue')
axs[1].set_ylabel('Velocity (v)')
axs[1].grid(True)

# Plot Height vs Time
axs[2].plot(df['Time(t)'], df['Height(x)'], marker='o', linestyle='-', color='green')
axs[2].set_ylabel('Height (x)')
axs[2].set_xlabel('Time (t)')
axs[2].grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
#plt.show()