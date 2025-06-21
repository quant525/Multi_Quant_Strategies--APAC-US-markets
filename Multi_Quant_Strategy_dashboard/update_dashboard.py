"""
update_dashboard.py

🔁 Auto-updates the strategy dashboard by:
1. Reading all strategy position .csv files from local folder
2. Generating combined total position and individual strategy plots
3. Updating README.md with the latest charts and metadata

📁 Make sure your position CSVs are in:
C:/Users/Sandy Chu/OneDrive/Desktop/MC_Postion/

🖥️ Run this script daily via terminal or Task Scheduler:
>>> python update_dashboard.py
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Folder with exported position .csv files
csv_folder = r"C:/Users/Sandy Chu/OneDrive/Desktop/MC_Postion"
image_folder = os.path.join(".", "images")
os.makedirs(image_folder, exist_ok=True)

# Strategy metadata
metadata = [
    ["TXFstrategyA", "Strategy A", "TAIEX Futures", "Trend Following", "30-min", "VWAP slope-based exit"],
    ["TXFstrategyB", "Strategy B", "TAIEX Futures", "Volatility Breakout", "30-min", "High/Low breakout"],
    ["TXFstrategyC", "Strategy C", "TAIEX Futures", "Trend Following", "30-min", "MA trend + breakout"],
    ["TXFstrategyD", "Strategy D", "TAIEX Futures", "Momentum", "30-min", "Intraday momentum filter"],
    ["HSIstrategyA", "Strategy E", "Hang Seng Index", "Trend Following", "30-min", "Rolling window breakout"],
    ["HSIstrategyB", "Strategy F", "Hang Seng Index", "Mean Reversion", "30-min", "Range reversal & filter"],
    ["NQstrategyA",  "Strategy G", "Nasdaq", "Trend Reversal", "30-min", "ADX + RSI contrarian logic"],
    ["NQstrategyB",  "Strategy H", "Nasdaq", "Volatility Breakout", "30-min", "Hourly volatility trigger"]
]
columns = ["filename", "Strategy Name", "Asset", "Type", "Frequency", "Logic"]
strategy_metadata = pd.DataFrame(metadata, columns=columns)

# Load position CSVs
def read_positions():
    combined = pd.DataFrame()
    for fn in strategy_metadata["filename"]:
        file = f"pos_{fn}.csv"
        full_path = os.path.join(csv_folder, file)
        if os.path.exists(full_path):
            df = pd.read_csv(full_path, names=["date", "time", "position"])
            df = df[df["date"] >= 20240301]
            try:
                df["datetime"] = pd.to_datetime(df["date"].astype(str) + df["time"].astype(str), format="%Y%m%d%H%M")
                df["strategy"] = fn
                combined = pd.concat([combined, df])
            except:
                continue
    return combined.sort_values("datetime")

def plot_total(df):
    pivot = df.pivot_table(index="datetime", columns="strategy", values="position", aggfunc="last").fillna(method="ffill").fillna(0)
    plt.figure(figsize=(14, 6))
    pivot.plot.area(ax=plt.gca())
    plt.title("Total Position by Strategy (Since Mar 2024)")
    plt.xlabel("Datetime")
    plt.ylabel("Position Size")
    plt.legend(loc="best")
    plt.tight_layout()
    plt.savefig(os.path.join(image_folder, "total_position_plot.png"))
    plt.close()
    return pivot

def plot_each(df):
    for strategy in df["strategy"].unique():
        sub = df[df["strategy"] == strategy]
        plt.figure(figsize=(10, 4))
        plt.plot(sub["datetime"], sub["position"], label=strategy)
        plt.title(f"{strategy} Position")
        plt.xlabel("Datetime")
        plt.ylabel("Position")
        plt.grid(True)
        plt.tight_layout()
        filename = f"{strategy}_position_plot.png"
        plt.savefig(os.path.join(image_folder, filename))
        plt.close()

def update_readme(df, pivot):
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    total = pivot.sum(axis=1).iloc[-1]
    lines = [f"# 📊 Strategy Position Dashboard",
             f"**Last Updated:** {now}  ",
             f"**Total Position:** {int(total)} contracts",
             "
## 📉 Total Position Chart",
             "![Total Position](images/total_position_plot.png)",
             "
## 📈 Individual Strategy Charts
"]
    for strategy in df["strategy"].unique():
        lines.append(f"### {strategy}")
        lines.append(f"![{strategy}](images/{strategy}_position_plot.png)")
    lines.append("
## 📋 Strategy Metadata Table
")
    lines.append(strategy_metadata.to_markdown(index=False))
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    df = read_positions()
    pivot = plot_total(df)
    plot_each(df)
    update_readme(df, pivot)
    print("✅ Dashboard updated successfully.")
