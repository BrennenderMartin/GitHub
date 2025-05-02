import matplotlib
matplotlib.use('Qt5Agg')  # interactive backend
import pandas as pd
import matplotlib.pyplot as plt

def create_graph(file):
    df = pd.read_csv(file)

    print("CSV preview:")
    print(df.head())

    fig, axs = plt.subplots(3, 1, figsize=(8, 10), sharex=True)
    fig.suptitle('Results vs Time\n delta_t = 0.02, steps = 30')

    axs[0].plot(df['Time(t)'], df['Acceleration(a)'], marker='o', linestyle='-', color='red')
    axs[0].set_ylabel('Acceleration (a)')
    axs[0].grid(True)

    axs[1].plot(df['Time(t)'], df['Velocity(v)'], marker='o', linestyle='-', color='blue')
    axs[1].set_ylabel('Velocity (v)')
    axs[1].grid(True)

    axs[2].plot(df['Time(t)'], df['Height(x)'], marker='o', linestyle='-', color='green')
    axs[2].set_ylabel('Height (x)')
    axs[2].set_xlabel('Time (t)')
    axs[2].grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

create_graph('result.csv')

plt.savefig("results.png")
plt.show()