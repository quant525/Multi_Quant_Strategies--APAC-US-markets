import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("data/pos_TXFstrategyA.csv", header=None, names=["Date", "Time", "Position"])
df["Date"] = df["Date"].apply(lambda x: f"20{x}" if len(str(x)) == 6 else str(x))
df["DateTime"] = pd.to_datetime(df["Date"] + df["Time"].apply(lambda x: f"{int(x):04}"), format="%Y%m%d%H%M")
df = df[df["DateTime"] >= pd.Timestamp("2024-03-01")]

# Plot
plt.figure(figsize=(12, 6))
plt.plot(df["DateTime"], df["Position"], marker="o", linestyle="-", label="Position Size")
plt.title("Position Change Over Time - TXF Strategy A")
plt.xlabel("Date")
plt.ylabel("Contracts")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("images/position_plot_english_fixed.png")

# Export latest 13:45 snapshot
df["HourMinute"] = df["DateTime"].dt.strftime("%H%M")
df_1345 = df[df["HourMinute"] == "1345"].sort_values("DateTime").tail(20)
df_1345[["DateTime", "Position"]].rename(columns={"DateTime": "DateTime (13:45)", "Position": "Contracts"}).to_csv("data/recent_1345_positions.csv", index=False)
