# Cross-Market Trend Divergence Strategy Dashboard

This GitHub project monitors and visualizes the position changes for the strategy: **Cross-Market Trend Divergence Model**, trading **TAIEX Futures**.

## 📈 Strategy Overview

- **Strategy Name**: Cross-Market Trend Divergence Model  
- **Asset**: TAIEX Futures  
- **Type**: Directional Alpha Model  
- **Data Frequency**: 30-minute K-bars  
- **Holding Duration**: 3 to 6 days

## 🔍 Position Time Series Chart
The following chart visualizes the strategy’s position changes since March 2024.

![Position Chart](charts/position_chart.png)

## 📊 Recent 20 Trading Days (13:45 Snapshot)
Daily positions taken at 13:45 each day.

![Position Table](charts/position_table.png)

## ⚙️ Automation
This repository includes:
- Python script to parse position CSV and auto-generate visuals
- GitHub Actions workflow to update chart + table daily

---

© Strategy logic remains proprietary. This repository only presents portfolio-level analytics and is safe to be shared publicly.
