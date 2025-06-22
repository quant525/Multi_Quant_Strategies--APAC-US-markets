import pandas as pd
import matplotlib.pyplot as plt
import os

# Load CSV
df = pd.read_csv('data/pos_TXFstrategyB.csv', header=None, names=["date", "time", "position"])

# Fix date formatting
df["date"] = df["date"].apply(lambda x: int(x) + 19000000)
df["date"] = pd.to_datetime(df["date"].astype(str), format="%Y%m%d")
df["time"] = df["time"].astype(str).str.zfill(4)
df["datetime"] = pd.to_datetime(df["date"].astype(str) + ' ' + df["time"].str[:2] + ':' + df["time"].str[2:], format="%Y-%m-%d %H:%M")

df.sort_values("datetime", inplace=True)

# Filter for date >= March 1, 2024
df = df[df["datetime"] >= "2024-03-01"]

# Plot position over time
plt.figure(figsize=(12, 6))
plt.plot(df["datetime"], df["position"], label="Position")
plt.title("Position Time Series - Cross-Market Trend Divergence Model")
plt.xlabel("Date")
plt.ylabel("Contracts")
plt.grid(True)
plt.legend()
os.makedirs("charts", exist_ok=True)
plt.tight_layout()
plt.savefig("charts/position_chart.png")

# Extract 13:45 snapshots for last 20 trading days
df_1345 = df[df["datetime"].dt.time == pd.to_datetime("13:45").time()]
df_recent = df_1345.tail(20).copy()

# Save table as image
import dataframe_image as dfi
dfi.export(df_recent[["datetime", "position"]].rename(columns={"datetime": "DateTime", "position": "Contracts"}), "charts/position_table.png")
