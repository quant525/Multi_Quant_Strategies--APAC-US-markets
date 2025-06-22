import pandas as pd
import matplotlib.pyplot as plt

# Load position file
df = pd.read_csv("data/pos_TXFstrategyC.csv", header=None, names=["date", "time", "position"])
df['datetime'] = pd.to_datetime(df['date'].astype(str) + df['time'].astype(str).str.zfill(4), format="%Y%m%d%H%M")
df = df.set_index('datetime')

# Daily filter at 13:45
filtered = df[df.index.time == pd.to_datetime("13:45").time()]
filtered.tail(20).to_csv("data/last20days_table.csv")

# Plot
filtered.tail(20)['position'].plot(marker='o', title="TXFstrategyC Position @13:45 - Last 20 Days")
plt.ylabel("Contracts Held")
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/last20days_chart.png")
